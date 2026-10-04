import struct
import json
import aiosqlite

from app.appconfig import DATABASE_PATH


async def save_news(
    db: aiosqlite.Connection, news: dict, analytics: dict
) -> int | None:
    """Сохраняет новость в две таблицы (rss_news и news_analytics) в рамках одной транзакции.
    Если новость с таким link/guid уже существует, возвращает None (дубликат).
    """
    # 1. Проверяем наличие дубликата по link или rss_uuid
    async with db.execute(
        "SELECT id FROM rss_news WHERE link = ? OR (rss_uuid IS NOT NULL AND rss_uuid = ?)",
        (news.get("link"), news.get("rss_uuid")),
    ) as cursor:
        if await cursor.fetchone():
            return None  # Новость уже есть в базе данных

    # 2. Вставка в основную таблицу rss_news
    # Обратите внимание: publicated_date_ts и created_date_ts должны быть INTEGER (Timestamp)
    sql_news = """
        INSERT INTO rss_news (
            rss_id, link, rss_uuid, title, description, preview, content, 
            publicated_ts, created_ts, text_hash
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    async with db.execute(
        sql_news,
        (
            news.get("rss_id"),
            news.get("link"),
            news.get("rss_uuid"),
            news.get("title"),
            news.get("description"),
            news.get("preview"),
            news.get("content"),
            news.get("publicated_ts"),
            news.get("created_ts"),
            news.get("text_hash"),
        ),
    ) as cursor:
        news_id = cursor.lastrowid

    # 3. Вставка в аналитическую таблицу news_analytics
    sql_analytics = """
        INSERT INTO news_analytics (
            news_id, cluster_id, publicated_ts, pub_hour_ts, pub_day_ts,
            category, industry, geo_targeting, target_audience,
            clickbait_score, fact_checked, importance_score, sentiment_score, 
            reading_time_min, matched_keyword
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    # Округляем Timestamp до часов и дней для корректных группировок (3600 сек = 1 час, 86400 сек = 1 день)
    pub_ts = analytics.get("publicated_ts") or news.get("publicated_ts", 0)
    pub_hour_ts = (pub_ts // 3600) * 3600
    pub_day_ts = (pub_ts // 86400) * 86400

    await db.execute(
        sql_analytics,
        (
            news_id,
            analytics.get("cluster_id"),
            pub_ts,
            pub_hour_ts,
            pub_day_ts,
            analytics.get("category"),
            analytics.get("industry"),
            analytics.get("geo_targeting"),
            analytics.get("target_audience"),
            analytics.get("clickbait_score", 0),
            analytics.get("fact_checked", 0),
            analytics.get("importance_score", 0),
            analytics.get("sentiment_score", 0.0),
            analytics.get("reading_time_min", 1),
            analytics.get("matched_keyword"),
        ),
    )

    # Фиксируем изменения в рамках транзакции
    await db.commit()
    return news_id


async def save_news_embedding(
    news_id: int, embedding_vector: list[float], model_name: str = "nomic-embed-text"
):
    """
    Упаковывает список float-чисел (вектор от Ollama) в бинарный формат BLOB
    и сохраняет в таблицу news_embeddings.
    """
    if not embedding_vector:
        return

    # Превращаем список float в байтовую строку.
    # Шаблон f'{len(embedding_vector)}f' означает, что мы упаковываем N чисел формата float (по 4 байта на каждое).
    blob_data = struct.pack(f"{len(embedding_vector)}f", *embedding_vector)

    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        sql = """
            INSERT OR REPLACE INTO news_embeddings (news_id, embedding, model_name)
            VALUES (?, ?, ?)
        """
        await db.execute(sql, (news_id, blob_data, model_name))
        await db.commit()


async def get_pending_news(limit: int) -> list[dict]:
    """Выбирает из базы данных пачку необработанных новостей (is_processed = 0)."""
    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        db.row_factory = aiosqlite.Row
        sql = "SELECT id, title, description, content FROM rss_news WHERE is_processed = 0 LIMIT ?"
        async with db.execute(sql, (limit,)) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_single_news_by_id(news_id: int) -> dict | None:
    """Ищет в базе данных одну конкретную новость по её ID."""
    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        db.row_factory = aiosqlite.Row
        sql = "SELECT id, title, description, content FROM rss_news WHERE id = ?"
        async with db.execute(sql, (news_id,)) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None


async def mark_news_as_failed(news_id: int, status_code: int = -2):
    """Помечает новость как ошибочную (например, если нет текста для анализа)."""
    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        await db.execute(
            "UPDATE rss_news SET is_processed = ? WHERE id = ?", (status_code, news_id)
        )
        await db.commit()


async def update_news_after_ai(
    news_id: int, ai_data: dict, embedding_vector: list[float] | None = None
) -> bool:
    """
    Записывает результаты ИИ-анализа (в rss_news и news_analytics)
    и упаковывает эмбеддинг в news_embeddings в рамках единой транзакции.
    """
    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        try:
            # 1. Обновляем основную текстовую таблицу rss_news
            sql_news = """
                UPDATE rss_news 
                SET is_processed = 1, ai_summary = ?, ai_sentiment = ?, 
                ai_category = ?, ai_industry = ?, ai_tags = ?, 
                ai_companies = ?, ai_persons = ?, ai_manipulation = ?
                WHERE id = ?
            """
            await db.execute(
                sql_news,
                (
                    ai_data["summary"],
                    ai_data["sentiment"],
                    ai_data["category"],
                    ai_data["industry"],
                    json.dumps(ai_data["ai_tags"], ensure_ascii=False),
                    json.dumps(ai_data["companies_mentioned"], ensure_ascii=False),
                    json.dumps(ai_data["persons_mentioned"], ensure_ascii=False),
                    ai_data["manipulation_type"],
                    news_id,
                ),
            )

            # 2. Обновляем числовую аналитическую таблицу news_analytics
            sql_analytics = """
                UPDATE news_analytics
                SET category = ?, industry = ?, geo_targeting = ?, target_audience = ?,
                    clickbait_score = ?, fact_checked = ?, importance_score = ?,
                    sentiment_score = ?, reading_time_min = ?
                WHERE news_id = ?
            """
            await db.execute(
                sql_analytics,
                (
                    ai_data["category"],
                    ai_data["industry"],
                    ai_data["geo_targeting"],
                    ai_data["target_audience"],
                    ai_data["clickbait_score"],
                    ai_data["fact_checked"],
                    ai_data["importance_score"],
                    ai_data["sentiment_score"],
                    ai_data["reading_time_min"],
                    news_id,
                ),
            )

            # 3. Если передан вектор, упаковываем его в BLOB и сохраняем
            if embedding_vector:
                blob_data = struct.pack(f"{len(embedding_vector)}f", *embedding_vector)
                sql_embedding = """
                    INSERT OR REPLACE INTO news_embeddings (news_id, embedding, model_name)
                    VALUES (?, ?, 'nomic-embed-text')
                """
                await db.execute(sql_embedding, (news_id, blob_data))

            # Фиксируем все изменения одной транзакцией
            await db.commit()
            return True

        except Exception as e:
            await db.rollback()
            print(
                f"Ошибка транзакции при сохранении ИИ-результатов для ID {news_id}: {e}"
            )
            raise e


# Постраничный вывод новостей с пагинацией и с фильтром по разным параметрам (категория, отрасль, гео, аудитория, дата публикации и т.д.)
# можно реализовать отдельной функцией, которая будет строить динамический SQL-запрос на основе переданных фильтров.


# Получение новости по id

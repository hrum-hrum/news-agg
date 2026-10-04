import asyncio
from app.services.ai_service import analyze_news_text, get_text_embedding
from app.db.db_rss_news import (
    get_pending_news,
    get_single_news_by_id,
    mark_news_as_failed,
    update_news_after_ai,
)


async def process_single_news_by_id(news_id: int) -> dict:
    """Точечно обрабатывает одну выбранную новость по её ID."""
    # Чтение данных из db.rss_news.py
    article = await get_single_news_by_id(news_id)

    if not article:
        return {"status": "error", "message": f"Новость с ID {news_id} не найдена."}

    text_to_analyze = (
        article["content"] if article["content"] else article["description"]
    )
    if not text_to_analyze:
        return {"status": "error", "message": "Отсутствует текст для анализа."}

    # ЭТАП 1: Сначала запускаем ИИ-анализ (он сгенерирует структуру и summary)
    try:
        ai_data = await analyze_news_text(article["title"], text_to_analyze)
    except Exception as e:
        ai_data = e

    # Строгая проверка ИИ-данных (Type Guard) для Pylance
    if isinstance(ai_data, BaseException) or ai_data is None:
        return {"status": "error", "message": f"Ошибка ИИ-анализа: {str(ai_data)}"}

    # ЭТАП 2: Берем текст для эмбеддинга (выжимку summary из ai_data, либо оригинал как запасной вариант)
    # Если вы добавили поле summary в NewsAnalysisSchema, оно будет в ai_data["summary"]
    text_for_embedding = ai_data.get("summary", text_to_analyze)

    # Запускаем генерацию эмбеддинга по короткому тексту
    valid_embedding = None
    try:
        embedding_vector = await get_text_embedding(text_for_embedding)
        if embedding_vector and not isinstance(embedding_vector, BaseException):
            valid_embedding = embedding_vector
    except Exception as e:
        print(f"Ошибка при генерации эмбеддинга: {e}")

    # 3. Запись данных в db.rss_news.py
    await update_news_after_ai(
        news_id=news_id, ai_data=ai_data, embedding_vector=valid_embedding
    )

    return {
        "status": "success",
        "message": f"Новость {news_id} успешно обработана ИИ.",
        "ai_analysis": ai_data,
    }


async def process_pending_news(limit: int = 10) -> dict:
    """Выбирает и обрабатывает пачку новых статей через Ollama."""
    processed_count = 0
    failed_count = 0

    # Чтение данных делегировано в db.rss_news.py
    pending_articles = await get_pending_news(limit)

    if not pending_articles:
        return {"processed": 0, "failed": 0, "status": "no_pending_news"}

    for article in pending_articles:
        news_id = article["id"]
        text_to_analyze = (
            article["content"] if article["content"] else article["description"]
        )

        if not text_to_analyze:
            await mark_news_as_failed(news_id)
            failed_count += 1
            continue

        # ЭТАП 1: Сначала запускаем ИИ-анализ (он сгенерирует структуру и summary)
        try:
            ai_data = await analyze_news_text(article["title"], text_to_analyze)
        except Exception as e:
            ai_data = e

        # 1. Единая строгая проверка ИИ-данных (Type Guard)
        if isinstance(ai_data, BaseException) or ai_data is None:
            print(f"Ошибка ИИ-анализа для новости ID {news_id}: {ai_data}")
            failed_count += 1
            continue

        # ЭТАП 2: Извлекаем сжатый текст для эмбеддинга
        # Берем summary из результатов анализа, либо оригинал (как запасной вариант)
        text_for_embedding = ai_data.get("summary", text_to_analyze)

        # Запускаем генерацию эмбеддинга по короткому тексту
        valid_embedding = None
        try:
            embedding_vector = await get_text_embedding(text_for_embedding)
            if embedding_vector and not isinstance(embedding_vector, BaseException):
                valid_embedding = embedding_vector
        except Exception as e:
            print(f"Ошибка генерации эмбеддинга для новости ID {news_id}: {e}")

        # 3. Вся запись и упаковка векторов делегирована в db.rss_news.py
        success = await update_news_after_ai(
            news_id=news_id,
            ai_data=ai_data,  # Pylance теперь знает, что это 100% dict
            embedding_vector=valid_embedding,  # Pylance знает, что это list[float] | None
        )

        if success:
            processed_count += 1
        else:
            failed_count += 1

    return {"processed": processed_count, "failed": failed_count, "status": "success"}

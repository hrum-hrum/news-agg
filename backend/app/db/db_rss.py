import aiosqlite

from app.appconfig import DATABASE_PATH


async def get_rss_list():
    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        # Настраиваем row_factory, чтобы строки возвращались в виде словарей,
        # и мы могли обращаться к полям по именам: row["title"], а не row[1]
        db.row_factory = aiosqlite.Row

        async with db.execute("SELECT id, link, title FROM rss_links") as cursor:
            rows = await cursor.fetchall()

            # Превращаем результат в обычный список Python-словарей
            rss_feeds = []
            for row in rows:
                rss_feeds.append(
                    {"id": row["id"], "title": row["title"], "link": row["link"]}
                )

            return rss_feeds


async def add_rss_link(link: str, title: str | None = None) -> int:
    """Добавляет новую RSS-ссылку в базу данных и возвращает её id."""
    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        async with db.execute(
            "INSERT INTO rss_links (link, title) VALUES (?, ?)", (link, title)
        ) as cursor:
            await db.commit()
            return cursor.lastrowid


async def delete_rss_link(rss_id: int) -> bool:
    """Удаляет RSS-ссылку по её ID. Возвращает True, если запись была удалена."""
    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        async with db.execute(
            "DELETE FROM rss_links WHERE id = ?", (rss_id,)
        ) as cursor:
            await db.commit()
            return cursor.rowcount > 0

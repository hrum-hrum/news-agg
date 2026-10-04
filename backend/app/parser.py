import asyncio
import time
from typing import Any, Dict, List
from email.utils import parsedate_to_datetime
from bs4 import BeautifulSoup
import feedparser_rs as feedparser  #
import httpx


def parse_xml_native(xml_content: str, rss_id: int) -> List[Dict[str, Any]]:
    """Парсинг XML силами Rust-библиотеки с вычислением Timestamp."""
    feed = feedparser.parse(xml_content)  #
    articles = []

    for entry in feed.entries:
        # Конвертируем строковую дату в Unix Timestamp
        pub_ts = int(time.time())
        if entry.get("published"):
            try:
                pub_ts = int(parsedate_to_datetime(entry["published"]).timestamp())
            except Exception:
                pass

        preview_url = None

        # 1. Проверяем вложения media:content или enclosure
        if entry.get("media"):
            for media_obj in entry["media"]:
                # Ищем среди медиафайлов те, которые являются картинками
                content_type = media_obj.get("content_type", "")
                if (
                    content_type.startswith("image/")
                    or media_obj.get("medium") == "image"
                ):
                    preview_url = media_obj.get("url")
                    break

            # Если по content_type не нашли, берем первую ссылку из медиа (часто это enclosure)
            if not preview_url and len(entry["media"]) > 0:
                preview_url = entry["media"][0].get("url")

        # Формируем плоский словарь под структуру таблицы rss_news
        articles.append(
            {
                "news": {
                    "rss_id": rss_id,
                    "link": entry.get("link", ""),
                    "rss_uuid": entry.get("id"),
                    "title": entry.get("title", "Без заголовка"),
                    "description": entry.get(
                        "summary"
                    ),  # Передаем описание из RSS в description
                    "content": None,  # Будет заполнено через BeautifulSoup4 позже
                    "publicated_ts": pub_ts,
                    "created_ts": int(time.time()),
                    "is_processed": 0,
                },
                # Дефолтная пустая аналитика до обработки через OpenAI
                "analytics": {"publicated_ts": pub_ts},
            }
        )
    return articles


async def parse_single_rss(rss_feed: Dict[str, Any]) -> List[Dict[str, Any]]:
    url = rss_feed["link"]
    rss_link_id = rss_feed["id"]

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
        try:
            response = await client.get(url, headers=headers)
            if response.status_code == 200:
                return await asyncio.to_thread(
                    parse_xml_native, response.text, rss_link_id
                )
            return []
        except Exception:
            return []


async def parse_all_feeds(rss_feeds: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    tasks = [parse_single_rss(feed) for feed in rss_feeds]
    results = await asyncio.gather(*tasks)

    all_articles = []
    for articles_list in results:
        all_articles.extend(articles_list)
    return all_articles


async def fetch_full_html(url: str) -> str | None:
    """Асинхронно скачивает HTML-код страницы статьи."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    # Используем follow_redirects=True, так как ссылки из RSS часто ведут через редиректы
    async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
        try:
            response = await client.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            return None
        except Exception as e:
            print(f"Ошибка загрузки страницы {url}: {e}")
            return None


def extract_article_content(html_content: str) -> str:
    """Универсально извлекает основной текст статьи из HTML, очищая от мусора."""
    soup = BeautifulSoup(html_content, "html.parser")

    # 1. Удаляем заведомо ненужные теги, которые создают текстовый шум
    for element in soup(
        [
            "script",
            "style",
            "nav",
            "header",
            "footer",
            "aside",
            "form",
            "iframe",
            "noscript",
        ]
    ):
        element.decompose()

    # 2. Стратегия поиска: сначала ищем стандартный HTML5 тег статьи
    article_body = soup.find("article")

    # Если тега <article> нет, ищем популярные классы контента
    if not article_body:
        # Ищем блоки, которые часто содержат текст статьи на новостных сайтах
        for class_keyword in [
            "post-content",
            "article-content",
            "entry-content",
            "article-text",
            "story-text",
            "post-text",
        ]:
            article_body = soup.find(class_=lambda c: c and class_keyword in c)
            if article_body:
                break

    # Если ничего не нашли, берем весь body (крайний случай)
    if not article_body:
        article_body = soup.find("body")

    if not article_body:
        return ""

    # 3. Собираем текст из параграфов <p> внутри найденного блока
    paragraphs = article_body.find_all("p")

    if paragraphs:
        # Соединяем параграфы через перенос строки, очищая от лишних пробелов
        text_content = "\n\n".join(
            [p.get_text().strip() for p in paragraphs if p.get_text().strip()]
        )
    else:
        # Если параграфов нет, забираем очищенный текст целиком
        text_content = article_body.get_text(separator="\n").strip()

    # Базовая очистка от слишком длинных пустых пространств
    lines = [line.strip() for line in text_content.splitlines() if line.strip()]
    return "\n".join(lines)


async def get_news_content(url: str) -> str | None:
    """Объединяет скачивание и парсинг контента в асинхронную задачу."""
    html = await fetch_full_html(url)
    if not html:
        return None

    # Выносим работу BeautifulSoup4 в отдельный поток, чтобы не блокировать event loop FastAPI
    content = await asyncio.to_thread(extract_article_content, html)
    return content if content else None

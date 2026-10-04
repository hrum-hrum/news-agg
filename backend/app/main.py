import os
import aiosqlite

from dotenv import load_dotenv

# позволит нам передавать значения по умолчанию в параметры пути и запросов
from typing import Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks, Query, status
from pydantic import BaseModel, HttpUrl

# Из базы db.sqlite3

from app.appconfig import DATABASE_PATH

from app.db.db_rss import get_rss_list, add_rss_link, delete_rss_link
from app.db.db_rss_news import save_news
from app.parser import get_news_content, parse_all_feeds
from app.services.bg_processor import process_pending_news, process_single_news_by_id

load_dotenv()

app = FastAPI(title="AI Parser Service")


# --- Схемы Pydantic для валидации запросов ---
class RSSCreate(BaseModel):
    link: HttpUrl  # Автоматически проверяет, что передан корректный URL-адрес
    title: Optional[str] = None  # Необязательное поле для названия ленты


# --- Добавляем схему Pydantic для строгого ответа эндпоинта ---
class ProcessNewsResponse(BaseModel):
    status: str
    message: str


# --- Схема Pydantic для строгого и безопасного ответа эндпоинта ---
class SingleNewsProcessResponse(BaseModel):
    status: str
    message: str
    embedding: str | None = None
    ai_analysis: dict | None = None  # Содержит полный JSON-отчет от Ollama


# @app.on_event("startup")
# async def startup_event():
#     # Создаем таблицы в БД при старте сервера
#     await init_db()


# --- Функция, которая будет запускаться в фоне ---
async def background_ai_processing(limit: int = 20):
    print("Фоновая задача: Запуск AI-анализа для новых статей...")
    result = await process_pending_news(limit=limit)
    print(f"Фоновая задача завершена: {result}")


@app.get("/")
async def root():
    return {"message": "Проект успешно запущен и готов к работе!"}


@app.get("/rss")
async def rss_links(id: Optional[int] = None):
    data = await get_rss_list()

    return {"data": data}


@app.post("/rss", status_code=status.HTTP_201_CREATED)
async def add_rss(rss_data: RSSCreate):
    """
    Роут для добавления новой RSS-ссылки.
    Принимает JSON с обязательным полем 'link' и необязательным 'title'.
    """
    try:
        # HttpUrl приводится к строке str() перед сохранением в SQLite
        new_id = await add_rss_link(link=str(rss_data.link), title=rss_data.title)
        return {
            "status": "success",
            "message": "RSS-ссылка успешно добавлена",
            "id": new_id,
        }
    except Exception as e:
        # Защита на случай, если ссылка уже существует (если в БД стоит UNIQUE ограничение)
        raise HTTPException(
            status_code=400,
            detail=f"Не удалось добавить ссылку. Возможно, она уже есть в базе. Ошибка: {str(e)}",
        )


@app.delete("/rss/{rss_id}")
async def remove_rss(rss_id: int):
    """
    Роут для удаления RSS-ссылки по её ID.
    Передается как path-параметр: /rss/5
    """
    deleted = await delete_rss_link(rss_id)

    if not deleted:
        raise HTTPException(
            status_code=404, detail=f"RSS-ссылка с ID {rss_id} не найдена в базе данных"
        )

    return {"status": "success", "message": f"RSS-ссылка с ID {rss_id} успешно удалена"}


@app.get("/parse-news")
async def parse_news_endpoint(background_tasks: BackgroundTasks):
    rss_feeds = await get_rss_list()
    if not rss_feeds:
        raise HTTPException(status_code=400, detail="В базе нет RSS-ссылок.")

    all_news = await parse_all_feeds(rss_feeds)
    if not all_news:
        return {"status": "success", "saved": 0}

    saved = 0
    duplicates = 0
    failed = 0
    saved_articles = []

    async with aiosqlite.connect(str(DATABASE_PATH)) as db:
        for item in all_news:
            news = item.get("news", {})
            analytics = item.get("analytics", {})

            if not news.get("link"):
                failed += 1
                continue

            try:
                # 1. Сначала проверяем на дубликат (чтобы зря не качать контент сайта)
                async with db.execute(
                    "SELECT id FROM rss_news WHERE link = ? OR (rss_uuid IS NOT NULL AND rss_uuid = ?)",
                    (news.get("link"), news.get("rss_uuid")),
                ) as cursor:
                    if await cursor.fetchone():
                        duplicates += 1
                        continue  # Новость уже есть, переходим к следующей

                # 2. Если новость новая — асинхронно выкачиваем полный текст статьи через BeautifulSoup4
                print(f"Скачиваем полный текст для: {news.get('link')}")
                full_text = await get_news_content(news.get("link"))

                # Записываем скачанный текст в поле контента
                news["content"] = full_text

                # 3. Сохраняем готовую запись в БД (в обе таблицы через ваш rss_news.py)
                news_id = await save_news(db, news, analytics)

                if news_id:
                    saved += 1
                    saved_articles.append({"id": news_id, "link": news.get("link")})

            except Exception as exc:
                failed += 1
                print(f"Ошибка обработки новости {news.get('link')}: {exc}")
                continue

    # ЕСЛИ были сохранены новые статьи — добавляем задачу анализа в фоновый поток FastAPI
    if saved > 0:
        background_tasks.add_task(background_ai_processing, limit=saved)

    return {
        "status": "success",
        "total_parsed": len(all_news),
        "saved": saved,
        "duplicates": duplicates,
        "failed": failed,
        "articles": saved_articles,
    }


@app.get("/process-news", response_model=ProcessNewsResponse)
async def force_process_news_endpoint(limit: int = Query(10, ge=1, le=50)):
    """
    Ручной эндпоинт для принудительного запуска AI-анализа скопившихся новостей.
    Полезно для тестов или ручного разбора очередей.
    """
    result = await process_pending_news(limit=limit)

    # Безопасное извлечение статуса
    if result.get("status") == "no_pending_news":
        return ProcessNewsResponse(
            status="success", message="Все новости уже были обработаны ранее."
        )

    # Задаем дефолтные значения на случай, если ключи отсутствуют,
    # гарантируя Pylance, что здесь не будет ошибки типов
    processed = result.get("processed", 0)
    failed = result.get("failed", 0)

    return ProcessNewsResponse(
        status="success",
        message=f"Успешно обработано ИИ: {processed}. Ошибок: {failed}.",
    )


@app.get("/process-news/{news_id}", response_model=SingleNewsProcessResponse)
async def process_single_news_endpoint(news_id: int):
    """
    Эндпоинт для принудительного точечного ИИ-анализа одной конкретной новости по её ID.
    Позволяет обрабатывать пропущенные статьи или заново пересчитывать старые.
    """
    # Вызываем логику обработки из processor.py
    result = await process_single_news_by_id(news_id=news_id)

    # Если сервис вернул ошибку (например, новость не найдена или упала Ollama)
    if result.get("status") == "error":
        raise HTTPException(
            status_code=400,
            detail=result.get(
                "message", f"Не удалось обработать новость с ID {news_id}"
            ),
        )

    # Возвращаем строго валидированный Pydantic-объект
    return SingleNewsProcessResponse(
        status="success",
        message=str(result.get("message")),
        embedding=result.get("embedding"),
        ai_analysis=result.get("ai_analysis"),
    )


# @app.get("/news", параметры)

# @app.get("/news/{news_id}")


# # http://127.0.0.1:8000/api/kurs/rub  (usd, eur)
# @app.get("/api/kurs/{currency_code}")
# def get_currency_rate(currency_code: str):
#     url = f"https://api.exchangerate-api.com/v4/latest/{currency_code.upper()}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "base_currency": data["base"],
#             "date": data["date"],
#             "rates": data["rates"],
#         }
#     else:
#         return {"error": "Курсы валют в данное время недоступны"}

import os
import json
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pydantic import BaseModel, Field

# Инициализируем клиента OpenAI, перенаправляя его на локальный адрес Ollama
# По умолчанию Ollama работает на порту 11434, API-ключ для нее не требуется (передаем любую строку)
# Загружаем переменные из файла .env в окружение
load_dotenv()

# Инициализируем клиент, получая данные из os.environ
client = AsyncOpenAI(
    base_url=os.environ.get("OPENAI_BASE_URL"), api_key=os.environ.get("OPENAI_API_KEY")
)

# Задаем имена моделей, которые вы скачали в Ollama
ANALYSIS_MODEL = "llama3.1:8b"
# ANALYSIS_MODEL = "qwen2.5-coder:32b-instruct-q4_K_M"
EMBEDDING_MODEL = "nomic-embed-text"


# --- Схема Pydantic для строгого формата ответа AI ---
class NewsAnalysisSchema(BaseModel):
    summary: str = Field(
        description="Краткая подробная выжимка статьи на русском языке объемом около 300-500 слов для генерации эмбеддингов. Без воды, только факты."
    )
    sentiment: str = Field(
        description="Тональность текста. Строго одно из значений: позитивный, нейтральный, смешанный, негативный, крайне негативный (эмоциональный шантаж, паника, крик, истерика)"
    )
    sentiment_score: float = Field(
        description="Числовая оценка тональности от -1.0 (ужасно/негативно) до 1.0 (отлично/позитивно)"
    )

    category: str = Field(
        description="Основная категория. Строго одно из: Политика, Экономика, Технологии, Спорт, Шоу-бизнес, Здоровье, Другое"
    )
    industry: str | None = Field(
        None,
        description="Отрасль для бизнес-новостей (например: Автопром, Ритейл, IT), либо null",
    )
    geo_targeting: str = Field(
        description="Географическая привязка (например: Россия, США, Москва, Глобальный)"
    )
    target_audience: str = Field(
        description="Целевая аудитория (например: инвесторы, разработчики, широкий круг)"
    )

    clickbait_score: int = Field(
        description="Индекс кликбейта заголовка от 1 (честный заголовок) до 10 (желтая пресса, обман)"
    )
    fact_checked: int = Field(
        description="1 если статья полна цифр, дат и проверяемых фактов. 0 если это субъективное мнение/слухи"
    )
    importance_score: int = Field(
        description="Рейтинг важности инфоповода от 1 (маловажное событие) до 10 (мировой масштаб)"
    )

    ai_tags: list[str] = Field(
        description="Список из 3-5 узких тегов/ключевых слов на русском языке"
    )
    companies_mentioned: list[str] = Field(
        description="Список упомянутых компаний и брендов. Если нет, пустой список []"
    )
    persons_mentioned: list[str] = Field(
        description="Список упомянутых известных личностей. Если нет, пустой список []"
    )
    manipulation_type: str = Field(
        description="Приемы манипуляции или 'чистые факты', 'нагнетание паники', 'эмоциональный шантаж'"
    )
    reading_time_min: int = Field(
        description="Примерное время на внимательное чтение статьи в минутах"
    )


# --- Основные функции сервиса ---


async def analyze_news_text(title: str, text: str) -> dict | None:
    """Отправляет заголовок и текст новости в Ollama и возвращает структурированную аналитику."""
    if not text:
        return None

    # Отрезаем кусок текста, если он экстремально огромный для контекста самого анализа
    # (опционально, но защитит от падения на этапе анализа)
    safe_text = text[:15000]

    prompt = f"""
    Проанализируй следующую новостную статью.
    Заголовок: {title}
    Полный текст:
    {safe_text}
    """

    try:
        # Вызываем локальную модель Ollama
        response = await client.beta.chat.completions.parse(
            model=ANALYSIS_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Ты — профессиональный русскоязычный медиа-аналитик. "
                    "Твоя задача — объективно анализировать статьи, "
                    "обязательно составлять подробное краткое содержание в поле 'summary' "
                    "и строго заполнять JSON-схему на русском языке."
                    "ВНИМАНИЕ: Тебе запрещено использовать английский язык в ответах. "
                    "Общайся исключительно на грамотном русском языке. "
                    "Все пояснения, размышления, JSON-поля и выводы должны быть только по-русски. "
                    "Начинай свой ответ сразу на русском языке.",
                },
                {"role": "user", "content": prompt},
            ],
            response_format=NewsAnalysisSchema,
            temperature=0.2,
        )

        # Безопасно получаем распарсенный ответ
        analysis_result = response.choices[0].message.parsed

        # Защита от None для Pylance и стабильности кода
        if analysis_result is None:
            print(
                "Ошибка: Ollama вернула пустой результат или не смогла заполнить схему."
            )
            return None

        # Теперь Pylance спокоен, так как мы доказали, что analysis_result — это объект Pydantic
        return analysis_result.model_dump()

    except Exception as e:
        print(f"Ошибка при AI-анализе текста через Ollama: {e}")
        return None


async def get_text_embedding(text: str) -> list[float] | None:
    """Запрашивает у Ollama векторный эмбеддинг для текста статьи."""
    if not text:
        return None

    try:
        response = await client.embeddings.create(model=EMBEDDING_MODEL, input=text)
        # Извлекаем массив float-чисел (вектор)
        return response.data[0].embedding
    except Exception as e:
        print(f"Ошибка генерации эмбеддинга через Ollama: {e}")
        return None

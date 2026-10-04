Обновить pip
python.exe -m pip install --upgrade pip

1. Создайте и активируйте виртуальное окружение Python

# На Windows:
python -m venv venv
venv\Scripts\activate

# На macOS/Linux:
python3 -m venv venv
source venv/bin/activate

Выбрать правильный интерпретатор в VS Code (Рекомендуемый)
1. Находясь в VS Code, нажмите комбинацию клавиш:
	• Windows/Linux: Ctrl + Shift + P
	• macOS: Cmd + Shift + P
2. В появившейся строке поиска введите Python: Select Interpreter (Выбрать интерпретатор) и нажмите Enter.
3. В списке выберите тот путь, который ведет к вашему виртуальному окружению. Обычно он выглядит так:
	• ./venv/Scripts/python.exe (на Windows)
	• ./venv/bin/python (на macOS/Linux)
	• Возле правильного варианта часто есть пометка ('venv': venv). 
Или нажать на + Create Virtual Environment
После выбора интерпретатора Pylance перезапустится и ошибка исчезнет в течение пары секунд.


2. Убедитесь, что ваше виртуальное окружение активировано, и выполните в терминале команду:

pip install -r requirements.txt

2. Создайте файл .env и добавьте туда ваш ключ от OpenAI:

OPENAI_API_KEY=your_openai_api_key_here

3. Так как вы установили fastapi[all], в комплекте уже идет асинхронный сервер Uvicorn.
Запустите проект командой в терминале:

uvicorn app.main:app --reload

Запустится по http://127.0.0.1:8000

Документация swagger
http://127.0.0
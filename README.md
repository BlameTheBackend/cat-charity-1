# Cat Charity

Небольшой учебный проект на FastAPI для управления благотворительными проектами и пожертвованиями.

## О проекте

Сервис позволяет:
- создавать благотворительные проекты;
- отслеживать собранную сумму;
- принимать пожертвования;
- автоматически закрывать проект, когда нужная сумма собрана;
- получать списки проектов и пожертвований через API.

Проект создан в учебных целях для изучения:
- FastAPI;
- SQLAlchemy;
- Pydantic;
- CRUD-операций;
- асинхронной работы с базой данных;
- тестирования API.

## Технологии

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- Pytest

## Быстрый старт

1. Создайте виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   Для Windows:

   ```bash
   .venv\Scripts\activate
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Запустите приложение:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Откройте документацию API:

   - http://127.0.0.1:8000/docs
   - http://127.0.0.1:8000/redoc

## Основные эндпоинты

### Благотворительные проекты
- GET /charity_project/
- POST /charity_project/
- PATCH /charity_project/{project_id}
- DELETE /charity_project/{project_id}

### Пожертвования
- GET /donation/
- POST /donation/

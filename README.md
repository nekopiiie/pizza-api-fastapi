# API для пиццерии
Backend-система для управления заказами в пиццерии.

## Технологии: Python, FastAPI, SQLModel, PostgreSQL

## Установка и запуск
1. Установите зависимости:
    pip install -r requirements.txt
    
2. Убедитесь, что запущен PostgreSQL.
3. Запустите приложение:
    uvicorn main_api:app --reload
    
4. Откройте в браузере: http://127.0.0.1:8000/docs для работы с API.

### API Endpoints
Клиенты
GET /customers/ - получить список клиентов
POST /customers/ - создать нового клиента

Блюда
GET /dishes/ - получить меню
POST /dishes/ - добавить блюдо

Заказы
GET /orders/ - получить список заказов
POST /orders/ - создать новый заказ

Курьеры
GET /couriers/ - получить список курьеров
POST /couriers/ - добавить курьера

Платежи
GET /payments/ - получить список платежей
POST /payments/ - создать платёж
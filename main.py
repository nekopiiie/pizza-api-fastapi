from sqlmodel import SQLModel
from database import engine, create_db_and_tables
from models import *

if __name__ == "__main__":
    create_db_and_tables()
    print("Таблицы успешно созданы!")
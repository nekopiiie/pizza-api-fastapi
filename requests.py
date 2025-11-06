from sqlmodel import Session, select
from database import engine
from models import Customer, Dish

def get_all_customers():
    with Session(engine) as session:
        statement = select(Customer)
        results = session.exec(statement)
        return results.all()

def get_dish_by_id(dish_id: int):
    with Session(engine) as session:
        statement = select(Dish).where(Dish.id == dish_id)
        return session.exec(statement).first()
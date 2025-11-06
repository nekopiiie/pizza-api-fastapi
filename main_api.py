from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import engine, get_session
from models import *

app = FastAPI(title="Pizza Delivery API", version="1.0.0")

@app.post("/customers/", response_model=Customer)
def create_customer(customer: Customer, session: Session = Depends(get_session)):
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.get("/customers/", response_model=list[Customer])
def read_customers(session: Session = Depends(get_session)):
    customers = session.exec(select(Customer)).all()
    return customers

@app.get("/customers/{customer_id}", response_model=Customer)
def read_customer(customer_id: int, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.post("/dishes/", response_model=Dish)
def create_dish(dish: Dish, session: Session = Depends(get_session)):
    session.add(dish)
    session.commit()
    session.refresh(dish)
    return dish

@app.get("/dishes/", response_model=list[Dish])
def read_dishes(session: Session = Depends(get_session)):
    dishes = session.exec(select(Dish)).all()
    return dishes

@app.post("/orders/", response_model=Order)
def create_order(order: Order, session: Session = Depends(get_session)):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order

@app.get("/orders/", response_model=list[Order])
def read_orders(session: Session = Depends(get_session)):
    orders = session.exec(select(Order)).all()
    return orders

@app.post("/couriers/", response_model=Courier)
def create_courier(courier: Courier, session: Session = Depends(get_session)):
    session.add(courier)
    session.commit()
    session.refresh(courier)
    return courier

@app.get("/couriers/", response_model=list[Courier])
def read_couriers(session: Session = Depends(get_session)):
    couriers = session.exec(select(Courier)).all()
    return couriers

@app.get("/couriers/{courier_id}", response_model=Courier)
def read_courier(courier_id: int, session: Session = Depends(get_session)):
    courier = session.get(Courier, courier_id)
    if not courier:
        raise HTTPException(status_code=404, detail="Courier not found")
    return courier

@app.post("/payments/", response_model=Payment)
def create_payment(payment: Payment, session: Session = Depends(get_session)):
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment

@app.get("/payments/", response_model=list[Payment])
def read_payments(session: Session = Depends(get_session)):
    payments = session.exec(select(Payment)).all()
    return payments

@app.get("/payments/{payment_id}", response_model=Payment)
def read_payment(payment_id: int, session: Session = Depends(get_session)):
    payment = session.get(Payment, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
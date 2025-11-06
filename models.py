from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

#все таблицы как классы Python

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    phone_number: str
    email: str = Field(unique=True, index=True)
    delivery_address: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    orders: List["Order"] = Relationship(back_populates="customer")

class Dish(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    category: str
    price: float  
    quantity: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    order_items: List["OrderItem"] = Relationship(back_populates="dish")

class Courier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    phone_number: str
    status: str = Field(default="свободен")  #свободен, занят, неактивен

    orders: List["Order"] = Relationship(back_populates="courier")

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    courier_id: Optional[int] = Field(default=None, foreign_key="courier.id")
    status: str = Field(default="новый")  #новый, готовится, готов, в пути, доставлен, отменен
    order_type: str  # delivery, pickup
    total_amount: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    customer: Customer = Relationship(back_populates="orders")
    courier: Optional[Courier] = Relationship(back_populates="orders")
    order_items: List["OrderItem"] = Relationship(back_populates="order")
    payment: Optional["Payment"] = Relationship(back_populates="order")

class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    dish_id: int = Field(foreign_key="dish.id")
    quantity: int
    price_at_order_time: float

    order: Order = Relationship(back_populates="order_items")
    dish: Dish = Relationship(back_populates="order_items")

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id", unique=True)
    amount: float
    method: str  # online, cash
    status: str = Field(default="pending")  # pending, completed, failed, refunded
    transaction_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    order: Order = Relationship(back_populates="payment")
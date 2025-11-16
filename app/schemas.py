from pydantic import BaseModel
from typing import List, Optional


class FoodCreate(BaseModel):
    name: str
    price: float


class FoodRead(FoodCreate):
    id: int

    class Config:
        orm_mode = True


class RestaurantCreate(BaseModel):
    name: str
    address: Optional[str] = None


class RestaurantRead(RestaurantCreate):
    id: int
    foods: List[FoodRead] = []

    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    customer_name: str
    items: List[dict]   # list of {"food_id": int, "qty": int}
    total: float

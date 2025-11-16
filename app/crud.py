from sqlalchemy.orm import Session
from . import models, schemas
import json


def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_rest = models.Restaurant(
        name=restaurant.name, address=restaurant.address)
    db.add(db_rest)
    db.commit()
    db.refresh(db_rest)
    return db_rest


def get_restaurants(db: Session):
    return db.query(models.Restaurant).all()


def create_food(db: Session, restaurant_id: int, food: schemas.FoodCreate):
    db_food = models.FoodItem(
        name=food.name, price=food.price, restaurant_id=restaurant_id)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food


def get_foods_by_restaurant(db: Session, restaurant_id: int):
    return db.query(models.FoodItem).filter(models.FoodItem.restaurant_id == restaurant_id).all()


def create_order(db: Session, order: schemas.OrderCreate):
    items_json = json.dumps(order.items)
    db_order = models.Order(customer_name=order.customer_name,
                            items=items_json, total=order.total)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def list_orders(db: Session):
    return db.query(models.Order).all()


def update_order_status(db: Session, order_id: int, status: str):
    order = db.query(models.Order).get(order_id)
    order.status = status
    db.commit()
    db.refresh(order)
    return order

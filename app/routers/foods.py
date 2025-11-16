from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..deps import get_db

router = APIRouter(prefix="/restaurants/{restaurant_id}/foods", tags=["foods"])


@router.post("/", response_model=schemas.FoodRead)
def add_food(restaurant_id: int, food: schemas.FoodCreate, db: Session = Depends(get_db)):
    return crud.create_food(db, restaurant_id, food)


@router.get("/", response_model=list[schemas.FoodRead])
def list_foods(restaurant_id: int, db: Session = Depends(get_db)):
    return crud.get_foods_by_restaurant(db, restaurant_id)

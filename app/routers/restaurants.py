from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..deps import get_db

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.post("/", response_model=schemas.RestaurantRead)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    return crud.create_restaurant(db, restaurant)


@router.get("/", response_model=list[schemas.RestaurantRead])
def list_restaurants(db: Session = Depends(get_db)):
    return crud.get_restaurants(db)

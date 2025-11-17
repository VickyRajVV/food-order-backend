from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..deps import get_db

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=dict)
def place_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = crud.create_order(db, order)
    return {"order_id": db_order.id, "status": db_order.status}

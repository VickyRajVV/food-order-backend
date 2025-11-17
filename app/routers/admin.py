from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from ..deps import get_db
import os

router = APIRouter(prefix="/admin", tags=["admin"])

API_KEY = "SECRET_ADMIN_KEY"  # for demo — load from env in real use


def check_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid admin API key")


@router.get("/orders")
def admin_list_orders(db: Session = Depends(get_db), x_api_key: str = Depends(check_api_key)):
    return crud.list_orders(db)


@router.put("/orders/{order_id}/status")
def admin_update_status(order_id: int, status: str, db: Session = Depends(get_db), x_api_key: str = Depends(check_api_key)):
    return crud.update_order_status(db, order_id, status)

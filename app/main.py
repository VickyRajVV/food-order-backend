from fastapi import FastAPI
from .database import Base, engine
from .routers import restaurants, foods, cart, admin

# create db tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Food Ordering API")

app.include_router(restaurants.router)
app.include_router(foods.router)
app.include_router(cart.router)
app.include_router(admin.router)

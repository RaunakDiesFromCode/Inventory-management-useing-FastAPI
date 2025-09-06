from fastapi import FastAPI
from app.database import Base, engine
from app.routers import items

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Item API")

# Include routers
app.include_router(items.router)

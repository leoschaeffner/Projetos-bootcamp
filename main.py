from fastapi import FastAPI
from app.routes.product import router as product_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Store API está no ar!"}

app.include_router(product_router)
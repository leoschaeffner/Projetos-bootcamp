from fastapi import APIRouter, HTTPException
from datetime import datetime

router = APIRouter()

# Simulação de banco de dados
db = {}

@router.post("/products")
def create_product(product: dict):
    if "name" not in product:
        raise HTTPException(status_code=500, detail="Erro ao inserir produto")
    product["id"] = str(len(db) + 1)
    db[product["id"]] = product
    return product

@router.patch("/products/{product_id}")
def update_product(product_id: str, update_data: dict):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    update_data["updated_at"] = update_data.get("updated_at", datetime.utcnow().isoformat())
    db[product_id].update(update_data)
    return db[product_id]
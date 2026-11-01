from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from services.product_service import ProductService
from dependencies import get_product_service

class ProductCreateInput(BaseModel):
    product_name: str
    product_price: int = Field(gt=0)

class UpdateOrderInput(BaseModel):
    user_id: int

class UpdatePriceInput(BaseModel):
    new_price: float

class ProductOut(BaseModel):
    id: int
    name: str
    price: float


router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
async def add_product(
    payload: ProductCreateInput,
    product_service: ProductService = Depends(get_product_service)
    ) -> dict[str, str]:
    await product_service.add_product(product_name=payload.product_name, product_price=payload.product_price)
    return {"status": "success", "message": "Product has been successfully added"}

@router.get("/", response_model=List[ProductOut])
async def get_products(
    product_service: ProductService = Depends(get_product_service)
) -> List[ProductOut]:
    products = await product_service.get_products()
    return [ProductOut(id=p.id, name=p.name, price=p.price) for p in products]

@router.put("/{product_id}")
async def change_product_price(
    product_id: int,
    payload: UpdatePriceInput,
    product_service: ProductService = Depends(get_product_service)
) -> dict[str, str]:
    await product_service.update_product_price(product_id=product_id, new_price=payload.new_price)
    return {"status": "success", "message": "Цена товара обновлена"}

@router.delete("/{product_id}")
async def remove_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_service)
) -> dict[str, str]:
    await product_service.delete_product(product_id)
    return {"status": "success", "message": "Товар успешно удален из базы"}
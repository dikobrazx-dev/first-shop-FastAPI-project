from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from services.product_service import ProductService
from dependencies import get_product_service

class ProductCreateInput(BaseModel):
    product_name: str
    product_price: int 

class UpdateOrderInput(BaseModel):
    user_id: int

class UpdatePriceInput(BaseModel):
    new_price: float


router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
async def add_product(
    payload: ProductCreateInput,
    product_service: ProductService = Depends(get_product_service)
    ):
    try:
        await product_service.add_product(product_name=payload.product_name, product_price=payload.product_price)
        return {"status": "success", "message": "Product has been successfully added"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.get("/")
async def get_products(
    product_service: ProductService = Depends(get_product_service)
):
    try:
        products =await product_service.get_products()
        return products
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.put("/{product_id}")
async def change_product_price(
    product_id: int,
    payload: UpdatePriceInput,
    product_service: ProductService = Depends(get_product_service)):
    try:
        await product_service.update_product_price(product_id=product_id, new_price=payload.new_price)
        return {"status": "success", "message": "Цена товара обновлена"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.delete("/{product_id}")
async def remove_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_service)):
    try:
        await product_service.delete_product(product_id)
        return {"status": "success", "message": "Товар успешно удален из базы"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
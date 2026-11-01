from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.order_service import OrderService
from dependencies import get_order_service

class OrderCreateInput(BaseModel):
    user_id: int

class OrderItemCreateInput(BaseModel):
    item_order_id: int
    item_product_id: int
    item_quantity: int

class UpdateOrderInput(BaseModel):
    user_id: int

class OrderOut(BaseModel):
    id: int
    user_id: int

class OrderItemOut(BaseModel):
    product_id: int
    quantity: int


router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
async def create_order(
    order_data: OrderCreateInput,
    order_service: OrderService = Depends(get_order_service)
    ):
    await order_service.add_order(user_id=order_data.user_id)
    return {"status": "success", "message": "Order has been successfully added"}

@router.get("/{order_id}", response_model=OrderOut)
async def get_order(
    order_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    order = await order_service.get_order(order_id)
    return OrderOut(id=order.id, user_id=order.user_id)

@router.put("/{id}")
async def change_order_owner(
    id: int,
    payload: UpdateOrderInput,
    order_service: OrderService = Depends(get_order_service)
    ):
    await order_service.update_order(id=id, user_id=payload.user_id)
    return {"status": "success", "message": "Order's owner has been updated"}

@router.delete("/{order_id}")
async def purge_order(
    order_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    await order_service.delete_order(order_id=order_id)
    return {"status": "success", "message":  "order has been successfully deleted"}

@router.post("/items")
async def add_order_item(
    payload: OrderItemCreateInput,
    order_service: OrderService = Depends(get_order_service)
    ):
    await order_service.add_order_item(
        item_order_id=payload.item_order_id,
        item_product_id=payload.item_product_id,
        item_quantity=payload.item_quantity
    )
    return {"status": "success", "message": "Product has been successfully added in order"}

@router.get("/{order_id}/items", response_model=List[OrderItemOut])
async def get_order_items(
    order_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    items = await order_service.get_order_items(order_id=order_id)
    return [OrderItemOut(product_id=item["product_id"], quantity=item["quantity"]) for item in items]

@router.delete("/{order_id}/{product_id}")
async def delete_order_item(
    order_id: int,
    product_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    await order_service.delete_order_item(item_order_id=order_id, item_product_id=product_id)
    return {"status": "success", "message": "Product has been successfully deleted from order"}

@router.get("/{order_id}/total_price")
async def total_price(
    order_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    total = await order_service.total_price(order_id)
    return total
from fastapi import APIRouter, Depends, HTTPException
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

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
async def create_user(
    order_data: OrderCreateInput,
    order_service: OrderService = Depends(get_order_service)
    ):
    try:
        await order_service.add_order(user_id=order_data)
        return {"status": "success", "message": "Order has been successfully added"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.put("/{id}")
async def change_order_owner(
    id: int,
    payload: UpdateOrderInput,
    order_service: OrderService = Depends(get_order_service)
    ):
    try:
        await order_service.update_order(id=id, user_id=payload.user_id)
        return {"status": "success", "message": "Order's owner has been updated"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.delete("/{order_id}")
async def purge_order(
    order_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    try:
        await order_service.delete_order(order_id=order_id)
        return {"status": "success", "message":  "order has been successfully deleted"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.post("/items")
async def add_order_item(
    payload: OrderItemCreateInput,
    order_service: OrderService = Depends(get_order_service)
    ):
    try:
        await order_service.add_order_item(
            item_order_id=payload.item_order_id,
            item_product_id=payload.item_product_id,
            item_quantity=payload.item_quantity
        )
        return {"status": "success", "message": "Product has been successfully added in order"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.get("/{order_id}/items")
async def get_order_items(
    order_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    try:
        items = await order_service.get_order_items(order_id=order_id)
        if not items:
            raise HTTPException(status_code=404, detail=f"There is not any product in order {order_id} or it does not exist")

        return items
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@router.delete("{order_id}/{product_id}")
async def delete_order_item(
    order_id: int,
    product_id: int,
    order_service: OrderService = Depends(get_order_service)
    ):
    try:
        await order_service.delete_order_item(item_order_id=order_id, item_product_id=product_id)
        return {"status": "success", "message": "Product has been successfully deleted from order"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

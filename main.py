from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import exceptions

from repositories.user_repository import UserRepository
from services.user_service import UserService

from repositories.product_repository import ProductRepository
from services.product_service import ProductService

from repositories.order_repository import OrderRepository
from services.order_service import OrderService

MyUserRepository = UserRepository()
MyUserService = UserService(MyUserRepository)

MyProductRepository = ProductRepository()
MyProductService = ProductService(MyProductRepository)

MyOrderRepository = OrderRepository()
MyOrderService = OrderService(MyOrderRepository, MyUserService, MyProductService)

app = FastAPI(title="Мой интернет магазин")

class UserCreateInput(BaseModel):
    user_name: str

class ProductCreateInput(BaseModel):
    product_name: str
    product_price: int 

class OrderCreateInput(BaseModel):
    user_id: int

class UpdateUserInput(BaseModel):
    user_name: str

class UpdateOrderInput(BaseModel):
    user_id: int

class OrderItemCreateInput(BaseModel):
    item_order_id: int
    item_product_id: int
    item_quantity: int

class UpdatePriceInput(BaseModel):
    new_price: float

@app.post("/users")
def add_user(payload: UserCreateInput):
    try:
        MyUserService.add_user(user_name=payload.user_name)
        return {"status": "success", "message": "User has been successfully added"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@app.get("/users")
def get_users():
    try:
        users = MyUserService.get_users()
        return users
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")




@app.put("/users/{user_id}")
def change_user_name(user_id: int, payload: UpdateUserInput):
    try:
        MyUserService.update_user(user_id=user_id, user_name=payload.user_name)
        return {"status": "success", "message": "User has been successfully updated"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@app.delete("/users/{user_id}")
def remove_user(user_id: int):
    try:
        MyUserService.delete_user(user_id=user_id)
        return {"status": "success", "message": "User and user's orders has been successfully deleted"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@app.post("/products")
def add_product(payload: ProductCreateInput):
    try:
        MyProductService.add_product(product_name=payload.product_name, product_price=payload.product_price)
        return {"status": "success", "message": "Product has been successfully added"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

class UpdateOrderInput(BaseModel):
    user_id: int


@app.put("/orders/{id}")
def change_order_owner(id: int, payload: UpdateOrderInput):
    try:
        MyOrderService.update_order(id=id, user_id=payload.user_id)
        return {"status": "success", "message": "Order's owner has been updated"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@app.delete("/orders/{order_id}")
def purge_order(order_id: int):
    try:
        MyOrderService.delete_order(order_id=order_id)
        return {"status": "success", "message":  "order has been successfully deleted"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@app.get("/products")
def get_products():
    try:
        products = MyProductService.get_products()
        return products
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")


# Изменить цену товара
@app.put("/products/{product_id}")
def change_product_price(product_id: int, payload: UpdatePriceInput):
    try:
        MyProductService.update_product_price(product_id=product_id, new_price=payload.new_price)
        return {"status": "success", "message": "Цена товара обновлена"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

# Полностью удалить товар
@app.delete("/products/{product_id}")
def remove_product(product_id: int):
    try:
        MyProductService.delete_product(product_id=product_id)
        return {"status": "success", "message": "Товар успешно удален из базы"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@app.post("/orders")
def add_order(payload: OrderCreateInput):
    try:
        MyOrderService.add_order(user_id=payload.user_id)
        return {"status": "success", "message": "Order has been successfully added"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@app.post("/orders/items")
def add_order_item(payload: OrderItemCreateInput):
    try:
        MyOrderService.add_order_item(
            item_order_id=payload.item_order_id,
            item_product_id=payload.item_product_id,
            item_quantity=payload.item_quantity
        )
        return {"status": "success", "message": "Product has been successfully added in order"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

@app.get("/orders/{order_id}/items")
def get_order_items(order_id: int):
    try:
        items = MyOrderService.get_order_items(order_id=order_id)
        if not items:
            raise HTTPException(status_code=404, detail=f"There is not any product in order {order_id} or it does not exist")

        return items
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error from server: {str(ex)}")

from pydantic import BaseModel, Field
from typing import List


class PaginationParams(BaseModel):
    skip: int
    limit: int


class UserCreateInput(BaseModel):
    user_name: str = Field(min_length=1)
    password: str = Field(min_length=8)


class UpdateUserInput(BaseModel):
    user_name: str


class UserOut(BaseModel):
    id: int
    name: str


class ProductCreateInput(BaseModel):
    product_name: str
    product_price: int = Field(gt=0)


class UpdatePriceInput(BaseModel):
    new_price: float


class ProductOut(BaseModel):
    id: int
    name: str
    price: float


class OrderCreateInput(BaseModel):
    user_id: int = Field(gt=0)


class OrderItemCreateInput(BaseModel):
    item_order_id: int = Field(gt=0)
    item_product_id: int = Field(gt=0)
    item_quantity: int = Field(gt=0)


class UpdateOrderInput(BaseModel):
    user_id: int


class OrderOut(BaseModel):
    id: int
    user_id: int


class OrderItemOut(BaseModel):
    product_id: int
    quantity: int
import exceptions
from repositories.order_repository import OrderRepository
from services.user_service import UserService
from services.product_service import ProductService
from models.order import Order
class OrderService:

    def __init__(
        self,
        order_repository: OrderRepository,
        user_service: UserService,
        product_service: ProductService
        ):
        self.order_repository = order_repository
        self.user_service = user_service
        self.product_service = product_service

    async def add_order(self, user_id):
        if await self.user_service.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return await self.order_repository.add_order(user_id)

    async def get_order(self, order_id):
        order = await self.order_repository.get_order(order_id)
        if order is None:
            raise exceptions.OrderNotFoundError(
                f"Order {order_id} not found"
            )
        return order 

    async def update_order(self, id, user_id):
        if await self.order_repository.get_order(id) is None:
            raise exceptions.OrderNotFoundError(
                f"Order {id} not found"
            )
        if await self.user_service.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return await self.order_repository.update_order(id, user_id)

    async def delete_order(self, order_id):
        if await self.order_repository.get_order(id) is None:
            raise exceptions.OrderNotFoundError(
                f"Order {id} not found"
            )
        return await self.order_repository.delete_order(order_id)

    async def add_order_item(self, item_order_id, item_product_id, item_quantity):
        if await self.order_repository.get_order(item_order_id) is None:
            raise exceptions.OrderNotFoundError(
                f"Order {item_order_id} not found"
            )
        if await self.product_service.get_product(item_product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"Product {item_product_id} not found"
            )
        if item_quantity <=0:
            raise exceptions.InvalidQuantityError(
                f"Quantity can not be negative or zero"
            )
        return await self.order_repository.add_order_item(item_order_id, item_product_id, item_quantity)

    async def get_order_items(self, order_id):
        if await self.order_repository.get_order(order_id) is None:
            raise exceptions.OrderNotFoundError(
                f"Order {order_id} not found"
            )
        return await self.order_repository.get_order_items(order_id)

    async def delete_order_item(self, item_order_id, item_product_id):
        if await self.order_repository.get_order(item_order_id) is None:
            raise exceptions.OrderNotFoundError(
                f"Order {item_order_id} not found"
            )
        if await self.product_service.get_product(item_product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"Product {item_product_id} not found"
            )
        return await self.order_repository.delete_order_item(item_order_id, item_product_id)

    async def total_price(self, order_id):
        total = 0
        order = await self.order_repository.get_order_with_items(order_id)
        if order is None:
            raise exceptions.OrderNotFoundError(
                f"Order {order_id} not found"
            )
        for item in order.items:
            total += item.quantity * item.product.price
        return total



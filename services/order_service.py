import exceptions
class OrderService:

    def __init__(self, order_repository, user_service, product_service):
        self.order_repository = order_repository
        self.user_service = user_service
        self.product_service = product_service

    async def add_order(self, user_id):
        if await self.user_service.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return await self.order_repository.add_order(user_id)

    async def get_orders(self):
        return await self.order_repository.get_orders()
        
    async def get_order(self, order_id):
        return await self.order_repository.get_order(order_id)

    async def update_order(self, id, user_id):
        if await self.user_service.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return await self.order_repository.update_order(id, user_id)

    async def delete_order(self, order_id):
        return await self.order_repository.delete_order(order_id)

    async def delete_all_orders(self):
        return await self.order_repository.delete_all_orders()

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
        return await self.order_repository.get_order_items(order_id)

    async def delete_order_item(self, item_order_id, item_product_id):
        return await  self.order_repository.delete_order_item(item_order_id, item_product_id)


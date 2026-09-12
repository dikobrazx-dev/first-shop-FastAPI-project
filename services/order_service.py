import exceptions
class OrderService:

    def __init__(self, order_repository, user_service, product_service):
        self.order_repository = order_repository
        self.user_service = user_service
        self.product_user = product_service

    def create_orders_table(self):
        return self.order_repository.create_orders_table()

    def add_order(self, user_id):
        if self.user_service.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return self.order_repository.add_order(user_id)

    def get_orders(self):
        return self.order_repository.get_orders()
        
    def get_order(self, order_id):
        return self.order_repository.get_order(order_id)

    def update_order(self, id, user_id):
        if self.user_service.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return self.order_repository.update_order(id, user_id)

    def delete_order(self, order_id):
        return self.order_repository.delete_order(order_id)

    def delete_all_orders(self):
        return self.order_repository.delete_all_orders()

    def delete_orders_table(self):
        return self.order_repository.delete_orders_table()



    def create_order_items_table(self):
        return self.order_repository.create_order_items_table()

    def add_order_item(self, item_order_id, item_product_id, item_quantity):
        return self.order_repository.add_order_item(item_order_id, item_product_id, item_quantity)

    def get_order_items(self, order_id):
        return self.order_repository.get_order_items(order_id)

    def delete_order_items_table(self):
        return self.order_repository.delete_order_items_table()

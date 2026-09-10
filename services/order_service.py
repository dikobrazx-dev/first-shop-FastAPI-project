from models.order import Order
from models.order_item import OrderItem
class OrderService:

    def __init__(self, repository):
        self.repository = repository

    def create_orders_table(self):
        return self.repository.create_orders_table()

    def add_order(self, order):
        return self.repository.add_order(Order(*order))

    def get_orders(self):
        return self.repository.get_orders()
        
    def get_order(self, order_id):
        return self.repository.get_order(order_id)

    def update_order(self, order):
        return self.repository.update_order(Order(*order))

    def delete_order(self, order_id):
        return self.repository.delete_order(order_id)

    def delete_all_orders(self):
        return self.repository.delete_all_orders()

    def delete_orders_table(self):
        return self.repository.delete_orders_table()



    def create_order_items_table(self):
        return self.repository.create_order_items_table()

    def add_order_item(self, item):
        return self.repository.add_order_item(OrderItem(*item))

    def get_order_items(self, order_id):
        return self.repository.get_order_items(order_id)

    def delete_order_items_table(self):
        return self.repository.delete_order_items_table()

from models.order import Order

class OrderService:

    def __init__(self, repository):
        self.repository = repository

    def create_table(self):
        return self.repository.create_table()

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

    def delete_all(self):
        return self.repository.delete_all()

    def delete_table(self):
        return self.repository.delete_table()

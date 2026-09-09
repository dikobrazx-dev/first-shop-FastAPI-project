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
from models.product import Product

class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def create_table(self):
        return self.repository.create_table()
from models.product import Product

class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def create_table(self):
        return self.repository.create_table()

    def add_product(self, product):
        return self.repository.add_product(Product(*product))

    def get_product(self, product_id):
        return self.repository.get_product(product_id)

    def get_products(self):
        return self.repository.get_products()

    def update_product(self, product):
        return self.repository.update_product(Product(*product))

    def delete_product(self, product_id):
        return self.repository.delete_product(product_id)
        
    def delete_all(self):
        return self.repository.delete_all()

    def delete_table(self):
        return self.repository.delete_table()

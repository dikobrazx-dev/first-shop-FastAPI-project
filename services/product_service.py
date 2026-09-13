

class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def create_table(self):
        return self.repository.create_table()

    def add_product(self, product_name, product_price):
        return self.repository.add_product(product_name, product_price)

    def get_product(self, product_id):
        return self.repository.get_product(product_id)

    def get_products(self):
        return self.repository.get_products()

    def update_product(self, product_id, product_name, product_price):
        return self.repository.update_product(product_id, product_name, product_price)

    def update_product_price(self, product_id, new_price):
        return self.repository.update_product_price(product_id, new_price)

    def delete_product(self, product_id):
        return self.repository.delete_product(product_id)
        
    def delete_all(self):
        return self.repository.delete_all()

    def delete_table(self):
        return self.repository.delete_table()

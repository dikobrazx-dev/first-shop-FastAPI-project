import exceptions
from repositories.product_repository import ProductRepository

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def add_product(self, product_name, product_price):
        return await self.repository.add_product(product_name, product_price)

    async def get_product(self, product_id):
        if await self.repository.get_product(product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"User {product_id} not found"
            )     
        return await self.repository.get_product(product_id)

    async def get_products(self):
        return await self.repository.get_products()

    async def update_product_price(self, product_id, new_price):
        if await self.repository.get_product(product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"User {product_id} not found"
            )            
        return await self.repository.update_product_price(product_id, new_price)

    async def delete_product(self, product_id):
        if await self.repository.get_product(product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"User {product_id} not found"
            )            
        return await self.repository.delete_product(product_id)
        
    async def delete_all(self):
        return await self.repository.delete_all()

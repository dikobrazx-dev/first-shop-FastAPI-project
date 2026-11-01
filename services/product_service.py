import exceptions
from repositories.product_repository import ProductRepository
from models.product import Product

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def add_product(self, product_name: str, product_price: int) -> None:
        return await self.repository.add_product(product_name, product_price)

    async def get_product(self, product_id: int) -> Product:
        if await self.repository.get_product(product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"User {product_id} not found"
            )     
        return await self.repository.get_product(product_id)

    async def get_products(self) -> list[Product]:
        return await self.repository.get_products()

    async def update_product_price(self, product_id: int, new_price: float) -> None:
        if await self.repository.get_product(product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"User {product_id} not found"
            )            
        return await self.repository.update_product_price(product_id, new_price)

    async def delete_product(self, product_id: int) -> None:
        if await self.repository.get_product(product_id) is None:
            raise exceptions.ProductNotFoundError(
                f"User {product_id} not found"
            )            
        return await self.repository.delete_product(product_id)
        
    async def delete_all(self) -> None:
        return await self.repository.delete_all()

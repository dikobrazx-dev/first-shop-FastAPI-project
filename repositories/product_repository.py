from sqlalchemy import select,delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.product import Product

class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_product(self, product_name, product_price):
        db_product = Product(name=product_name,price=product_price)
        try:
            self.session.add(db_product)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

    async def get_products(self):
        try:
            stmt = select(Product)
            result = await self.session.execute(stmt)
            products = result.scalars().all()
            return products
        except Exception:
            raise

    async def get_product(self, product_id):
        try:
            product = await self.session.get(Product, product_id)
            return product
        except Exception:
            raise

    async def update_product_price(self, product_id, new_price):
        try:
            product = await self.session.get(Product, product_id)
            product.price= new_price
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

    async def delete_product(self, product_id):
        try:
            stmt = delete(Product).where(Product.id==product_id)
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise



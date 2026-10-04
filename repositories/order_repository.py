from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
import sqlite3  
get_connection = 1
from models.order import Order
from models.order_item import OrderItem
class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_order(self, user_id):
        db_order = Order(user_id=user_id)
        try:
            self.session.add(db_order)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise



    async def get_order(self, order_id):
        try:
            order = await self.session.get(Order, order_id)
            return order
        except Exception:
            raise


    
    def get_orders(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM orders")
            orders = cursor.fetchall()
            return [Order(*order) for order in orders]
        except sqlite3.Error:
            raise

        finally:
            connection.close()

        

    async def update_order(self, id, user_id):
        try:
            db_order = await self.session.get(Order, id)
            db_order.user_id = user_id
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise



    async def delete_order(self, id):
        try:
            order = await self.session.get(Order, id)
            self.session.delete(order)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

    def delete_all_orders(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM orders")
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()

    async def add_order_item(self, item_order_id: int, item_product_id: int, item_quantity: int):
        db_order_item = OrderItem(order_id = item_order_id, product_id = item_product_id, quantity = item_quantity)
        try:
            self.session.add(db_order_item)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
    
    async def get_order_items(self, order_id):
        try:
            stmt = select(OrderItem).where(OrderItem.order_id == order_id)
            result = await self.session.execute(stmt)
            items = result.scalars().all()
            return items
        except Exception:
            raise

    async def delete_order_item(self, item_order_id, item_product_id):
        try:
            stmt = delete(OrderItem).where(OrderItem.order_id == item_order_id).where(OrderItem.product_id == item_product_id)
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise


from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
import sqlite3  
get_connection = 1
from models.order import Order
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



    def get_order(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM orders WHERE id=?",(order_id,))
            order = cursor.fetchone()
            if order is not None:
                return Order(*order)
        except sqlite3.Error:
            raise

        finally:
            connection.close()

    
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

    def create_order_items_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items(
                order_id INTEGER REFERENCES orders(id),
                product_id INTEGER REFERENCES products(id),
                quantity INTEGER NOT NULL
            )"""
            )
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()



    def add_order_item(self, item_order_id, item_product_id, item_quantity):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO order_items(order_id, product_id, quantity) VALUES(?,?,?)",\
            (item_order_id, item_product_id, item_quantity))
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


    
    def get_order_items(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT products.id, products.name, products.price, order_items.quantity
            FROM order_items
            JOIN products ON products.id = order_items.product_id
            WHERE order_items.order_id = ?
            """, (order_id,))
            order_items = cursor.fetchall()
            return order_items
        except sqlite3.Error:
            raise

        finally:
            connection.close()

    def delete_order_item(self, item_order_id, item_product_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM order_items WHERE order_id=? AND product_id=?",(item_order_id, item_product_id))
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


    def delete_order_items_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DROP TABLE order_items")
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


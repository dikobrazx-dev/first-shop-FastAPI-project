from database.database import get_connection
from models.product import Product
import sqlite3
class ProductRepository:
    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
            )"""
            )
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()

        

    def add_product(self, product_name, product_price):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO products(name, price) VALUES(?,?)",(product_name, product_price))
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()



    def get_products(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return [Product(*product) for product in products]
        except sqlite3.Error:
            raise

        finally:
            connection.close()


    def get_product(self, product_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM products WHERE id=?",(product_id,))
            product = cursor.fetchone()
            if product is not None:
                return Product(*product)
        except sqlite3.Error:
            raise

        finally:
            connection.close()



    def update_product(self,  product_id, product_name, product_price):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE products SET name=?, price=? WHERE id=?",(product_name, product_price, product_id))
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()

        


    def delete_product(self, product_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM products WHERE id=?",(product_id,))
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


    def delete_all(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM products")
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


    def delete_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DROP TABLE products")
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


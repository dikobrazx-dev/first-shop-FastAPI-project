from database.database import get_connection
from models.product import Product
class ProductRepository:
    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL
        )"""
        )
        connection.commit()
        connection.close()
        

    def add_product(self, product):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products(name, price) VALUES(?,?)",(product.name, product.price))
        connection.commit()
        connection.close()


    def get_products(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        connection.close()
        return [Product(*product) for product in products]

    def get_product(self, product_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id=?",(product_id,))
        user = cursor.fetchone()
        connection.close()
        return Product(*user)


    def update_product(self, product):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET name=?, price=? WHERE id=?",(product.name, product.price, product.id))
        connection.commit()
        connection.close()


    def delete_product(self, product_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id=?",(product_id,))
        connection.commit()
        connection.close()

    def delete_all(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products")
        connection.commit()
        connection.close()

    def delete_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE products")
        connection.commit()
        connection.close()

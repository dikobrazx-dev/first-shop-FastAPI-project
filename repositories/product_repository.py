from database.database import get_connection
from models.product import Product
class ProductRepository:
    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        )"""
        )
        connection.commit()
        connection.close()
        
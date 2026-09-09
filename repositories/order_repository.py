from database.database import get_connection
from models.order import Order
class OrderRepository:
    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY,
            user_id TEXT REFERENCES users(id)
        )"""
        )
        connection.commit()
        connection.close()

    def add_order(self, order):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO orders(user_id) VALUES(?)",(order.user_id,))
        connection.commit()
        connection.close()

    
    def get_orders(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        connection.close()
        return [Order(*order) for order in orders]


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
    def get_user(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE id=?",(order_id,))
        order = cursor.fetchone()
        connection.close()
        return Order(*order)
    
    def get_orders(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        connection.close()
        return [Order(*order) for order in orders]

    def update_order(self, order):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE orders SET user_id=? WHERE id=?",(order.user_id, order.id))
        connection.commit()
        connection.close()


    def delete_order(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM orders WHERE id=?",(order_id,))
        connection.commit()
        connection.close()

    def delete_all(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM orders")
        connection.commit()
        connection.close()


    def delete_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE orders")
        connection.commit()
        connection.close()


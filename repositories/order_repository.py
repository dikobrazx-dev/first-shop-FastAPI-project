from database.database import get_connection
from models.order import Order
class OrderRepository:
    def create_orders_table(self):
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


    def get_order(self, order_id):
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

    def delete_all_orders(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM orders")
        connection.commit()
        connection.close()

    def delete_orders_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE orders")
        connection.commit()
        connection.close()
 

 

    def create_order_items_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items(
            order_id INTEGER REFERENCES orders(id),
            product_id INTEGER REFERENCES products(id),
            quantity INTEGER NOT NULL
        )"""
        )
        connection.commit()
        connection.close()


    def add_order_item(self, item):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO order_items(order_id, product_id, quantity) VALUES(?,?,?)",\
        (item.order_id, item.product_id, item.quantity))
        connection.commit()
        connection.close()

    
    def get_order_items(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        SELECT products.id, products.name, products.price, order_items.quantity
        FROM order_items
        JOIN products ON products.id = order_items.product_id
        WHERE order_items.order_id = ?
        """, (order_id,))
        order_items = cursor.fetchall()
        connection.close()
        return order_items


    def delete_order_items_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE order_items")
        connection.commit()
        connection.close()

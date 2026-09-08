from database.database import get_connection

class OrderRepository:
    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY,
            user_id TEXT REFERENCES users.id
        )"""
        )
        connection.commit()
        connection.close()

    def add_order(self, order):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO orders(user_id) VALUES(?)",(order,))
        connection.commit()
        connection.close()

    



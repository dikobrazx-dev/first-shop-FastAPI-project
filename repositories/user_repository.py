from database.database import get_connection

from models.user import User
class user_repository:
    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )"""
        )
        connection.commit()
        connection.close()

    def add_user(self, user):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users(name) VALUES(?)",(user.name,))
        connection.commit()
        connection.close()

    def get_users(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        connection.close()
        return [User(*user) for user in users]

    def get_user(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?",(user_id,))
        user = cursor.fetchone()
        connection.close()
        return User(*user)

    def update_user(self, user):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET name=? WHERE id=?",(user.name, user.id))
        connection.commit()
        connection.close()

    def delete_user(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
        connection.commit()
        connection.close()

    def delete_all(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users")
        connection.commit()
        connection.close()

    def delete_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE users")
        connection.commit()
        connection.close()

from database.database import get_connection
import sqlite3
from models.user import User
class UserRepository:
    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )"""
            )
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()



    def add_user(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users(name) VALUES(?)",(user_id,))
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()



    def get_users(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return [User(*user) for user in users]
        except sqlite3.Error:
            raise

        finally:
            connection.close()
 

    def get_user(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE id=?",(user_id,))
            user = cursor.fetchone()
            if user is not None:
                return User(*user)
        except sqlite3.Error:
            raise

        finally:
            connection.close()
 


    def update_user(self, user_id, user_name):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE users SET name=? WHERE id=?",(user_name, user_id))
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()



    def delete_user(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
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
            cursor.execute("DELETE FROM users")
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
            cursor.execute("DROP TABLE users")
            connection.commit()
        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


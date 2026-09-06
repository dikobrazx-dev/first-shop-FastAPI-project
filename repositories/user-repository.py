from database.database import get_connection


def create_table():
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

def add_user(name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(name) VALUES(?)",(name,))
    connection.commit()
    connection.close()

def get_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return users

def get_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?",(user_id,))
    user = cursor.fetchone()
    connection.close()
    return user

def update_user(user_id,new_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET name=? WHERE id=?",(new_name,user_id))
    connection.commit()
    connection.close()

def delete_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
    connection.commit()
    connection.close()

def delete():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users")
    connection.commit()
    connection.close()

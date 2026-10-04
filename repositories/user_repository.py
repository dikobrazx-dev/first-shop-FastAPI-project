from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
import sqlite3  
get_connection = 1
from models.user import User
class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, name):
        db_user = User(name=name)
        try:
            self.session.add(db_user)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

    async def get_users(self):
        try:
            stmt = select(User)
            result = await self.session.execute(stmt)
            users = result.scalars().all()
            return users
        except Exception:
            raise
 
    async def get_user(self, user_id):
        try:
            user = await self.session.get(User, user_id)
            return user
        except Exception:
            raise

    async def update_user(self, user_id, user_name):
        try:
            user = await self.session.get(User, user_id)
            user.name = user_name
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

    async def delete_user(self, user_id):
        try:
            user = await self.session.get(User, user_id)
            self.session.delete(user)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

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


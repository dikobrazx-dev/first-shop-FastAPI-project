import exceptions
from repositories.user_repository import UserRepository
from models.user import User
from auth import get_password_hash, verify_password

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def add_user(self, user_name: str, password: str) -> None:
        hashed_password = get_password_hash(password)
        return await self.repository.add_user(user_name, hashed_password)

    async def register_user(self, user_name: str, password: str) -> User:
        hashed_password = get_password_hash(password)
        return await self.repository.add_user(user_name, hashed_password)

    async def authenticate_user(self, user_name: str, password: str) -> User | None:
        user = await self.repository.get_user_by_name(user_name)
        if user is None:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def get_user(self, user_id: int) -> User:
        user = await self.repository.get_user(user_id)
        if user is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return user

    async def get_user_by_name(self, name: str) -> User | None:
        return await self.repository.get_user_by_name(name)

    async def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return await self.repository.get_users(skip=skip, limit=limit)

    async def update_user(self, user_id: int, user_name: str) -> None:
        if await self.repository.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )            
        return await self.repository.update_user(user_id, user_name)

    async def delete_user(self, user_id: int) -> None:
        if await self.repository.get_user(user_id) is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )            
        return await self.repository.delete_user(user_id)

    

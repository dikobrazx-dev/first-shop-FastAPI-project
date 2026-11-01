import exceptions
from repositories.user_repository import UserRepository
from models.user import User

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def add_user(self, user_name: str) -> None:
        return await self.repository.add_user(user_name)

    async def get_user(self, user_id: int) -> User:
        user = await self.repository.get_user(user_id)
        if user is None:
            raise exceptions.UserNotFoundError(
                f"User {user_id} not found"
            )
        return user

    async def get_users(self) -> list[User]:
        return await self.repository.get_users()

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

    

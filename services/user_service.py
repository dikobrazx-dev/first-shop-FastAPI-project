

class UserService:
    def __init__(self, repository):
        self.repository = repository

    async def add_user(self, user_name):
        return await self.repository.add_user(user_name)

    async def get_user(self, user_id):
        return await self.repository.get_user(user_id)

    async def get_users(self):
        return await self.repository.get_users()

    async def update_user(self, user_id, user_name):
        return await self.repository.update_user(user_id, user_name)

    async def delete_user(self, user_id):
        return await self.repository.delete_user(user_id)
        
    async def delete_all(self):
        return await self.repository.delete_all()
    

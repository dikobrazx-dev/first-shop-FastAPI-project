

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_table(self):
        return self.repository.create_table()

    async def add_user(self, user_name):
        return await self.repository.add_user(user_name)

    async def get_user(self, user_id):
        return await self.repository.get_user(user_id)

    async def get_users(self):
        return await self.repository.get_users()

    def update_user(self, user_id, user_name):
        return self.repository.update_user(user_id, user_name)

    def delete_user(self, user_id):
        return self.repository.delete_user(user_id)
        
    def delete_all(self):
        return self.repository.delete_all()

    def delete_table(self):
        return self.repository.delete_table()

    

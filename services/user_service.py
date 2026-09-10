from models.user import User

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_table(self):
        return self.repository.create_table()

    def add_user(self, user):
        return self.repository.add_user(User(*user))

    def get_user(self, user_id):
        return self.repository.get_user(user_id)

    def get_users(self):
        return self.repository.get_users()

    def update_user(self, user):
        return self.repository.update_user(User(*user))

    def delete_user(self, user_id):
        return self.repository.delete_user(user_id)
        
    def delete_all(self):
        return self.repository.delete_all()

    def delete_table(self):
        return self.repository.delete_table()

    

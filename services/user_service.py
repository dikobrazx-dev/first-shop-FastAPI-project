from models.user import User

class UserService:
    def __init__(self, repository):
        self.repository = repository

        
    def get_user(self, user_id):
        return self.repository.get_user(user_id)

    def get_users(self):
        return self.repository.get_users()

    def add_user(self, user):
        return self.repository.add_user(User(*user))

    def delete_user(self, user_id):
        return self.repository.delete_user(user_id)

    def update_user(self, user):
        return self.repository.update_user(User(*user))

    def delete_all(self):
        return self.repository.delete()



    

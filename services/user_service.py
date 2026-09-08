from models.user import User

class UserService:
    def __init__(self, repository):
        self.repository = repository

        
    def get_user(self, user):
        return self.repository.get_user(User(*user))

    def get_user(self):
        return self.repository.get_users()

    def add_user(self, user):
        return self.repository.add_user(User(*user))

    def delete_user(self, user):
        return self.repository.delete_user(User(*user))

    def update_user(self, user):
        return self.repository.update_user(User(*user))

    def delete_all(self):
        return self.repository.delete()



    

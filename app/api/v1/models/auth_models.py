from .base import BaseModel


class UserModel(BaseModel):
    """
    User Model
    """
    def __init__(self):
        self.users = []
        self.blacklist= []

    def get_all_users(self):
        return self.users
    def get_all_tokens(self):
        return self.blacklist
    #add a user to table
    def add_user(self,data):
        self.users.append(data)

    #add token to table
    def add_to_black_list(self,data):
        self.blacklist.append(data)
        return data

    def get_by_name(self, name,data):
        return next(filter(lambda x:x['username'] == name, data), None)

    #get blacklist token 
    def get_token(self, name,data):
        return next(filter(lambda x:x['token'] == name, data), None)

    def get_by_email(self, name,data):
        return next(filter(lambda x:x['email'] == name, data), None)

user_model = UserModel()

from hmac import compare_digest
from src.resources.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user is not None and compare_digest(password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

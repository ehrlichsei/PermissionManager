import random
import string

from datetime import datetime
import logging

def generate_random_token(length=32):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class TokenManager:
    def __init__(self):
        self.tokens = {}

    def generate_token(self, user, permission_name, expiration_time):
        permission = user.get_permission_by_name(permission_name)
        if permission:
            token = generate_random_token()  # 生成随机令牌的方法，具体实现可根据需要调整
            logging.debug(f"生成令牌：{token}")
            self.tokens[token] = {
                'permission_name': permission_name,
                'expiration_time': expiration_time,
                'username': user.username
            }
            return token
        else:
            return None

    def revoke_token(self, token):
        if token in self.tokens:
            del self.tokens[token]

    def is_token_valid(self, token):
        if token in self.tokens:
            token_info = self.tokens[token]
            current_time = datetime.now()
            expiration_time = token_info['expiration_time']
            if current_time < expiration_time:
                return True
            else:
                self.revoke_token(token)
                return False
        else:
            return False

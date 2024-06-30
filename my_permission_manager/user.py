class User:
    def __init__(self, username):
        self.username = username
        self.permissions = []    # 用户的权限列表

    def add_permission(self, permission):
        self.permissions.append(permission)

    def remove_permission(self, permission_name):
        self.permissions = [p for p in self.permissions if p.name != permission_name]

    def get_permission_by_name(self, permission_name):
        for permission in self.permissions:
            if permission.name == permission_name:
                return permission
        return None
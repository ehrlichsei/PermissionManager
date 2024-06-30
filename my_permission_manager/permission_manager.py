class PermissionManager:
    def __init__(self):
        self.permissions = []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def get_permission_by_name(self, name):
        for permission in self.permissions:
            if permission.name == name:
                return permission
        return None

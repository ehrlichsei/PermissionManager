class Permission:
    def __init__(self, name, description, scope):
        self.name = name          # 权限名称
        self.description = description  # 权限描述
        self.scope = scope        # 权限作用范围，如特定的API或功能点

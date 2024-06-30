from my_permission_manager.permission_manager import PermissionManager
from my_permission_manager.token_manager import TokenManager
from my_permission_manager.user import User
from my_permission_manager.permission import Permission

from datetime import datetime, timedelta

import logging

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    # 创建权限管理器和用户
    permission_manager = PermissionManager()
    user1 = User("alice")

    # 定义并添加权限
    read_api_permission = Permission("read_api", "允许访问特定API的读取功能", "specific_api_read")
    permission_manager.add_permission(read_api_permission)
    user1.add_permission(read_api_permission)

    # 用户生成并分享权限令牌
    expiration_time = datetime.now() + timedelta(hours=1)  # 令牌有效期为1小时
    token_manager = TokenManager()
    token = token_manager.generate_token(user1, "read_api", expiration_time)

    # 模拟验证令牌
    if token_manager.is_token_valid(token):
        print("令牌有效，可以访问API")
    else:
        print("令牌无效或已过期")

    # 撤销令牌（例如用户取消分享）
    token_manager.revoke_token(token)

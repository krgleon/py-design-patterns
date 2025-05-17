# Real object: the sensitive file
class SecureFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        return f"Reading contents of {self.filename}..."

# Proxy: controls access to SecureFile
class AccessProxy:
    def __init__(self, user_role: str, real_file: SecureFile):
        self.user_role = user_role
        self.real_file = real_file

    def read(self):
        if self.user_role != "admin":
            return "❌ Access denied: insufficient permissions"
        return self.real_file.read()

# User without permissions
proxy_guest = AccessProxy("guest", SecureFile("confidential.txt"))
print(proxy_guest.read())

# User with permissions
proxy_admin = AccessProxy("admin", SecureFile("confidential.txt"))
print(proxy_admin.read())

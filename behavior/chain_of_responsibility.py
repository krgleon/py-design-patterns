# Base handler class: defines interface and links to the next handler
class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # allows chaining

    def handle(self, user):
        if self.next_handler:
            return self.next_handler.handle(user)
        return True

class AuthHandler(Handler):
    def handle(self, user):
        if not user.get("authenticated"):
            print("❌ User is not authenticated")
            return False
        print("✅ Authenticated")
        return super().handle(user)

class ActiveHandler(Handler):
    def handle(self, user):
        if not user.get("active"):
            print("❌ User is not active")
            return False
        print("✅ Active")
        return super().handle(user)

class PermissionHandler(Handler):
    def handle(self, user):
        if "admin" not in user.get("roles", []):
            print("❌ User lacks admin role")
            return False
        print("✅ Has admin permission")
        return super().handle(user)

# Define the user
user = {
    "authenticated": False,
    "active": True,
    "roles": ["editor", "admin"]
}

# Set up the chain
chain = AuthHandler()
chain.set_next(ActiveHandler()).set_next(PermissionHandler())

# Run the chain
if chain.handle(user):
    print("✅ Access granted!")
else:
    print("🚫 Access denied.")

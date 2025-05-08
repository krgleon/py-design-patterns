import sqlite3

# Base Singleton class using __new__ to ensure only one instance per subclass
class Singleton:
    _instances = {}  # Dictionary to hold instances of each subclass

    def __new__(cls, *args, **kwargs):
        # If an instance doesn't exist yet, create and store it
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]  # Return the stored instance

# A database connection class that uses the Singleton behavior
class DatabaseConnection(Singleton):
    connection = None  # Shared connection across all instances

    def __init__(self):
        # Only create a connection if it hasn't been initialized yet
        if self.connection is None:
            self.connection = sqlite3.connect("users.db")

    def execute_query(self, query):
        # Execute a SQL query on the current database connection
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def close(self):
        # Properly close the database connection
        self.connection.close()

# First instance of DatabaseConnection
db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Second instance (will be the same as db1)
db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Khronozg')")

# Check that both variables point to the same instance
print(db1 is db2)  # True, both are the same instance

# Closing the connection from both variables (same underlying connection)
db1.close()
db2.close()

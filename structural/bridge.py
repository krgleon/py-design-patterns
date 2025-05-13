# The implementation interface (the "bridge" side)
class DatabaseConnector:
    def connect(self):
        raise NotImplementedError

    def execute(self, query: str):
        raise NotImplementedError

class SQLiteConnector(DatabaseConnector):
    def connect(self):
        print("Connected to SQLite database.")

    def execute(self, query: str):
        print(f"Executing on SQLite: {query}")

class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        print("Connected to PostgreSQL database.")

    def execute(self, query: str):
        print(f"Executing on PostgreSQL: {query}")

class DatabaseClient:
    def __init__(self, connector: DatabaseConnector):
        self._connector = connector

    def connect(self):
        self._connector.connect()

    def run_query(self, query: str):
        self._connector.execute(query)

# Client selects the connector type
postgres = DatabaseClient(PostgreSQLConnector())
sqlite = DatabaseClient(SQLiteConnector())

# Use them the same way, regardless of backend
postgres.connect()
postgres.run_query("SELECT * FROM users")

sqlite.connect()
sqlite.run_query("INSERT INTO users (name) VALUES ('Khronozg')")


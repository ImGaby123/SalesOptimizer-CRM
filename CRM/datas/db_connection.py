import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host="127.0.0.1", user="root", password="", database="crm_db", port=3306):
        """Initialize the database connection."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Establish a connection to the MySQL database."""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            self.cursor = self.conn.cursor(dictionary=True)  # Returns results as dictionaries
            print("✅ Database connection successful!")
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")

    def execute_query(self, query, params=None):
        """Execute INSERT, UPDATE, DELETE queries safely using parameterized queries."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except Error as e:
            print(f"❌ Error executing query: {e}")
            return False

    def fetch_one(self, query, params=None):
        """Fetch a single record."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None

    def fetch_all(self, query, params=None):
        """Fetch all records."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None

    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("✅ Database connection closed.")

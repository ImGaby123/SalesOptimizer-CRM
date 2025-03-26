import mysql.connector
from mysql.connector import Error

class DB_Connection:
    def __init__(self, host="127.0.0.1", user="root", password="", database="crm", port=3306):
        """Initialize the database connection."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = self.connect()  # Establish connection once

    def connect(self):
        """Establish a connection to MySQL and return the connection object."""
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print("✅ Database connection successful!")
            return conn
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            return None

    def execute_query(self, query, params=None):
        """Safely execute INSERT, UPDATE, DELETE queries using a context manager."""
        if not self.conn:
            print("❌ No database connection.")
            return False

        try:
            with self.conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, params)
                self.conn.commit()
                return True
        except Error as e:
            print(f"❌ Error executing query: {e}")
            return False

    def fetch_one(self, query, params=None):
        """Fetch a single record safely."""
        if not self.conn:
            print("❌ No database connection.")
            return None

        try:
            with self.conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None

    def fetch_all(self, query, params=None):
        """Fetch all records safely."""
        if not self.conn:
            print("❌ No database connection.")
            return None

        try:
            with self.conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None

    def __del__(self):
        """Auto-close the database connection when the object is deleted."""
        if self.conn:
            self.conn.close()
            print("✅ Database connection closed.")


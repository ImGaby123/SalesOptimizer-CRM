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
        self.conn = None
        self.connect()

    def connect(self):
        """Establish a connection to MySQL and handle reconnection."""
        try:
            if self.conn and self.conn.is_connected():
                return  # Already connected
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print("✅ Database connection successful!")
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            self.conn = None

    def ensure_connection(self):
        """Ensure that the connection is active before executing queries."""
        if not self.conn or not self.conn.is_connected():
            print("⚠️ Reconnecting to database...")
            self.connect()

    def execute_query(self, query, params=None):
        """Safely execute INSERT, UPDATE, DELETE queries."""
        self.ensure_connection()
        if not self.conn:
            print("❌ No database connection.")
            return False

        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            self.conn.commit()
            return True
        except Error as e:
            print(f"❌ Error executing query: {e}")
            self.conn.rollback()
            return False
        finally:
            cursor.close()

    def fetch_one(self, query, params=None):
        """Fetch a single record safely."""
        self.ensure_connection()
        if not self.conn:
            return None

        cursor = self.conn.cursor(dictionary=True, buffered=True)  # << buffered=True
        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None
        finally:
            cursor.close()


    def fetch_all(self, query, params=None):
        """Fetch all records safely."""
        self.ensure_connection()
        if not self.conn:
            return None

        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None
        finally:
            cursor.close()

    def close_connection(self):
        """Manually close the database connection."""
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("✅ Database connection closed.")

    def __del__(self):
        """Ensure the database connection is closed when the object is deleted."""
        self.close_connection()

import mysql.connector

class db_connection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="BORRIS",
            database="crm", 
            port=3306
            )


# For Debugging Purposes
dog = db_connection()
print("Connection Credentials: ",dog.conn)



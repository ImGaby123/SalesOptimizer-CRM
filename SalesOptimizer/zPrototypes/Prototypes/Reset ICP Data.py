from DB.db_connection import db_connection


"""
WARNING!!!!!
Do not Run this file unless needed

"""


# Connection
db = db_connection()
conn = db.conn

# cursor1
cursor = conn.cursor()

# Read and execute SQL file
with open("Data/ICP Data Insert.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

# Split into individual statements and execute
for statement in sql_script.split(";"):
    if statement.strip():
        cursor.execute(statement)
        print(statement)
        
conn.commit()

print("-----------------Data has been Reset Succesfully!-----------------")
# Close
cursor.close()
conn.close()
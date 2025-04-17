from db_connection import db_connection

# Connection
db = db_connection()
conn = db.conn

# cursor1
cursor1 = conn.cursor()
cursor2 = conn.cursor()

# Attributes
cursor1.execute("select * from icp ORDER BY attribute_id ASC;")
attributes = cursor1.fetchall()

# Rules
cursor2.execute("select * from icp_rules " \
                "ORDER BY icp_attribute_id ASC," \
                "attribute_score DESC;")
rules = cursor2.fetchall()


# Print
print("------ ICP Attributes ------")
for attribute in attributes:
    print(attribute[1])

print("------ ICP Rules ------")
for rule in rules:
    attribute_name = next((attribute[1] for attribute in attributes if attribute[0] == rule[0]), None)

    print("{} = {} : {}".format(attribute_name,rule[1], rule[2]))

# Close
cursor1.close()
cursor2.close()
conn.close()
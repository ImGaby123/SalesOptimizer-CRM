from DB.db_connection import db_connection

class ICP_Data:
    def __init__(self):
        
        # Connection
        dog = db_connection()
        self.conn = dog.conn
    

    def get_attributes(self):
        # cursor1
        cursor1 = self.conn.cursor()
        # Attributes
        cursor1.execute("select * from icp ORDER BY attribute_id ASC;")
        attributes = cursor1.fetchall()

        # Close
        cursor1.close()

        # Return Attributes
        #print(f"Attributes: {attributes}")
        return attributes

    def get_rules(self):
        cursor2 = self.conn.cursor()

        # Rules
        cursor2.execute("select * from icp_rules " \
                        "ORDER BY icp_attribute_id ASC," \
                        "attribute_score DESC;")
        
        rules = cursor2.fetchall()
        
        cursor2.close()

        # Return Rules
        #print(f"Rules: {rules}")
        return rules
    

import mysql.connector

class db_functions:
    def __init__(self, db_connection):
        self.conn = db_connection.conn
        self.cursor = self.conn.cursor(dictionary=True)


    # ------------------------ Get Data Here ------------------------
    def get_attributes(self):
        """Retrieve all attributes from the database."""
        self.cursor.execute("SELECT attribute FROM icp")
        return [row["attribute"] for row in self.cursor.fetchall()]

    def get_attribute_data(self, attribute):
        """Retrieve attribute_id and weight for a specific attribute."""
        self.cursor.execute("SELECT attribute_id, weight FROM icp WHERE attribute = %s", (attribute,))
        return self.cursor.fetchone()

    def get_all_attributes(self):
        """Retrieve all attribute_id and attribute pairs."""
        self.cursor.execute("SELECT attribute_id, attribute FROM icp")
        return self.cursor.fetchall()

    def get_icp_rules(self, attribute_id):
        try:
            self.cursor.execute("SELECT attribute_value, attribute_score FROM icp_rules WHERE icp_attribute_id = %s", (attribute_id,))

            # Fetch results from the current query
            rules = self.cursor.fetchall()

            # Make sure any unread results are cleared
            while self.cursor.nextset():
                pass

            return rules
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def get_rule_by_value(self, attribute_id, value, score):
        try:
            self.cursor.execute("""
                SELECT 1 FROM icp_rules
                WHERE icp_attribute_id = %s AND attribute_value = %s AND attribute_score = %s
            """, (attribute_id, value, score))

            result = self.cursor.fetchone()

            # Ensure no unread results remain
            while self.cursor.nextset():
                pass

            return result
        except Exception as e:
            print(f"Error fetching rule: {e}")
            return None

    
    # Insert Update and Delete Data Here

    def update_weight(self, updates):
        """Update weights for multiple attributes in the database."""
        try:
            self.cursor.executemany("UPDATE icp SET weight = %s WHERE attribute_id = %s", updates)
            self.conn.commit()
        except mysql.connector.Error as err:
            raise Exception(f"Failed to update weights: {err}")

    def delete_rules(self, attribute_id):
        try:
            self.cursor.execute("DELETE FROM icp_rules WHERE icp_attribute_id = %s", (attribute_id,))

            # Clear any remaining result sets if present
            while self.cursor.nextset():
                pass

            self.connection.commit()
        except Exception as e:
            print(f"Error deleting rules: {e}")

    def insert_rules(self, rules):
        """Insert new rules into the database."""
        try:
            self.cursor.executemany("""INSERT INTO icp_rules (icp_attribute_id, attribute_value, attribute_score)
                                        VALUES (%s, %s, %s)""", rules)
            self.conn.commit()
        except mysql.connector.Error as err:
            raise Exception(f"Failed to insert rules: {err}")

    def clear_cursor(self):
        try:
            while self.cursor.nextset():
                pass
        except:
            pass

    def update_clear_weight(self):
        """Update weights for multiple attributes to 0."""

        query = """
            UPDATE 
                `crm`.`icp`
            SET
                `weight` = 0
            WHERE 
                `attribute_id` > 0;
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Weights Cleared")
        except mysql.connector.Error as err:
            raise Exception(f"Failed to update weights: {err}")
        

        
    def update_leadScores(self, lead_id, lead_score):
        """Update weights for multiple attributes to 0."""

        print("Lead ID: {} ; Lead Score: {}".format(lead_id, lead_score))
        query = f"""
            UPDATE 
                `crm`.`leads`
            SET
                `lead_score` = {lead_score}
            WHERE 
                `lead_id` = {lead_id};
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Lead Score Updated")
        except mysql.connector.Error as err:
            raise Exception(f"Failed to update weights: {err}")
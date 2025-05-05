from DB.db_connection import db_connection


class Lead_Data:
    def __init__(self):
                
        # Connection
        dog = db_connection()
        self.conn = dog.conn
    
    def getLeadCountPerScore(self):
        # cursor1
        cursor1 = self.conn.cursor()

        query = """
                    SELECT lead_score, COUNT(*) AS lead_count
                    FROM crm.leads
                    WHERE lead_score BETWEEN 1 AND 10
                    GROUP BY lead_score
                    ORDER BY lead_score;
                """
        # Attributes
        cursor1.execute(query)
        attributes = cursor1.fetchall()

        # Close
        cursor1.close()

        # Return Attributes
        #print(f"Attributes: {attributes}")
        return attributes

    def getLeadOverTimeData(self):
        
                # cursor1
        cursor1 = self.conn.cursor()

        query = """
            SELECT DATE(created_at) AS lead_date, COUNT(*) AS total_leads
            FROM crm.leads
            GROUP BY lead_date
            ORDER BY lead_date;
        """

        # Attributes
        cursor1.execute(query)
        attributes = cursor1.fetchall()

        # Close
        cursor1.close()

        # Return Attributes
        #print(f"Attributes: {attributes}")
        return attributes
    
    def getOpportunityWonCostOverLeadScore(self):

                        # cursor1
        cursor1 = self.conn.cursor()
        
        query = """
                SELECT 
                    l.lead_score,
                    SUM(o.opportunity_cost) AS total_opportunity_cost
                FROM crm.opportunity o
                JOIN crm.leads l ON o.lead_id = l.lead_id
                WHERE o.opportunity_status = 'Closed Won'
                GROUP BY l.lead_score
                ORDER BY l.lead_score;
            """
        
        # Attributes
        cursor1.execute(query)
        attributes = cursor1.fetchall()

        # Close
        cursor1.close()

        # Return Attributes
        #print(f"Attributes: {attributes}")
        return attributes
    
    def getOpportunityStatusPerLeadScore(self):
                        # cursor1
        cursor1 = self.conn.cursor()
                        # cursor2
        cursor2 = self.conn.cursor()

        queryWon = """
            SELECT 
                l.lead_score,
                COUNT(*) AS opportunity_count
            FROM crm.opportunity o
            JOIN crm.leads l ON o.lead_id = l.lead_id
            WHERE l.lead_score BETWEEN 1 AND 10
            AND o.opportunity_status IN ('Closed Won')
            GROUP BY l.lead_score, o.opportunity_status
            ORDER BY l.lead_score, o.opportunity_status;
        """
                # Attributes
        cursor1.execute(queryWon)
        OpportunitiesWon = cursor1.fetchall()

        # Close
        cursor1.close()


        queryLoss = """
            SELECT 
                l.lead_score,
                COUNT(*) AS opportunity_count
            FROM crm.opportunity o
            JOIN crm.leads l ON o.lead_id = l.lead_id
            WHERE l.lead_score BETWEEN 1 AND 10
            AND o.opportunity_status IN ('Closed Loss')
            GROUP BY l.lead_score, o.opportunity_status
            ORDER BY l.lead_score, o.opportunity_status;
        """
                        # Attributes
        cursor2.execute(queryLoss)
        OpportunitiesLoss = cursor2.fetchall()

        # Close
        cursor2.close()

        return OpportunitiesWon, OpportunitiesLoss
    

    def getSaleCost(self):
                # cursor1
        cursor1 = self.conn.cursor()
        
        query = """
                    SELECT 
                        DATE(updated_at) AS day,
                        SUM(opportunity_cost) AS total_cost
                    FROM 
                        crm.opportunity
                    WHERE 
                        opportunity_status = 'Closed Loss'
                    GROUP BY 
                        DATE(updated_at)
                    ORDER BY 
                        day;
                """
         # Attributes
        cursor1.execute(query)
        attributes = cursor1.fetchall()
        
        # Close
        cursor1.close()
        
        # Return Attributes
        return attributes
from Data.ICP_Data import ICP_Data






"""
# This File contains a Lead Scoring algorithm based on the Weighted Sum Model.


# Weighted Sum Model:
# The sum of each value of Xn multiplied by its corresponding weight Wn.

#      m
# LS = E  (Xn * Wn)
#      n=1

# Where:
# LS = Lead Score
# E = Summation Symbol
# Xn = Lead Feature/Attribute
# Wn = Weight Assigned
# n  = n-th value
# m  = total number of attribute considered


# Special Conditions for Wn:
# The sum of all weights assigned to each lead attribute must be equal to 1

#  m
#  E (Wn) = 1
#  n=1

"""


"""
How To use the Methods

# 1. Create an Object for the Class
Dog = LeadScoring()

# 2. Assign Lead Instance to a variable
Lead_Instance = {1:'QC', 2: 'IT', 3: 'TECH', 4: 25}

# 3. Convert Each Attribute to its corresponding score
Converted_AttributeValue = Dog.lead_Score_Assignment(Lead_Instance)

# 4. Compute the Converted Value into a lead score
Lead_Score = Dog.lead_Score_Computation(Converted_AttributeValue)


"""














class LeadScoring:
    def __init__(self):

        # In Here We initialize the ICP Rules, Attributes, and Weights
        self.ICP_Rules = {}
        self.ICP_Attributes = {}
        self.ICP_Weights = {}

        # Initializing Individual Lead Score
        self.Lead_Attributes = {}

        # Assign Existing Values in DB
        dog = ICP_Data()
        rules = dog.get_rules()
        attributes = dog.get_attributes()

        self.ICP_Attributes = attributes

        # Rule Assignment
        for i in rules:
            if i[0] not in self.ICP_Rules:
                self.ICP_Rules[i[0]] = {}
            self.ICP_Rules[i[0]][i[1]] = i[2]

        # Weights Assignment
        for i in attributes:
            if i[0] not in self.ICP_Weights:
                self.ICP_Weights[i[0]] = {}
            self.ICP_Weights[i[0]] = float(i[2])
    
    def lead_Score_Assignment(self, value = {}):
        #print("Lead Scoring Called")

        # Method's Input must be in Dict form. e.g
        # value = {1: 'QC', 2: 'IT', 3:'TECH', 4: 20}
        Lead_Instance = value

        # Compare Values
        # Loop Through the Rules and assign the corresponding score
        for key,value in self.ICP_Rules.items():
            #print(f"{key}: {value}")
            if key in Lead_Instance.keys():
                lookup_key = Lead_Instance[key]
                if lookup_key in value:
                    Lead_Instance[key] = value[lookup_key]
                else:
                    # If Not Found, Then assume assign value of ANY
                    Lead_Instance[key] = value['ANY']
            else:
                # If Key doesn't Exist, Then assume assign value of ANY
                Lead_Instance[key] = value['ANY']

        # Lead's Attributes Scores Output must be
        # Lead_Attributes = {1 : 10, 2: 10, 3:10, 4:5}
        #print("Lead Scoring Ended")

        return Lead_Instance


    def lead_Score_Computation(self, Converted_Lead_Instance):
        
        # Method Input must be in dict form and the values must be in INT data type. e.g.
        # Converted_Lead_Instance = {1: 10, 2: 10, 3: 10, 4: 5}

        #print("Lead Computation Called")
        Weighted_Lead_Scores = []

        for n in Converted_Lead_Instance:
            Weighted_Lead_Scores.append(Converted_Lead_Instance[n] * self.ICP_Weights[n])

        Sum_Lead_Score = sum(Weighted_Lead_Scores)

        #print("Lead Computation Ended")

        # This will return the sum of all Lead_Score
        return Sum_Lead_Score
    



if __name__ == "__main__":
    Dog = LeadScoring()

    print("Attributes")
    print(Dog.ICP_Attributes)


    print("Weights: ", Dog.ICP_Weights)
    
    # 1. Assign Lead Instance
    Lead_Instance = {1:'QC', 2: 'IT', 3: 'TECH', 4: 25}
    print("Lead Instance: ", Lead_Instance)

    # 2. Convert Each Attribute to its corresponding score
    Converted_AttributeValue = Dog.lead_Score_Assignment(Lead_Instance)
    print("Converted: ",Converted_AttributeValue)

    # 3. Compute the Converted Value
    Computed_AttributeValue = Dog.lead_Score_Computation(Converted_AttributeValue)
    print("Lead Score: ", Computed_AttributeValue)


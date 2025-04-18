from models.LeadScoring import LeadScoring as LS



Dog_Score = LS()

# 1. Assign Lead Instance
Lead_Instance = {1:'QC', 2: 'IT', 3: 'TECH', 4: 25}

# 2. Convert Each Attribute to its corresponding score
Converted_AttributeValue = Dog_Score.lead_Score_Assignment(Lead_Instance)

# 3. Compute the Converted Value
Lead_Score = Dog_Score.lead_Score_Computation(Converted_AttributeValue)


print("Lead Score : ", Lead_Score)
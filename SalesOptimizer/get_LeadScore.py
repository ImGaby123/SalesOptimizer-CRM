from models.LeadScoring import LeadScoring as LS


Dog_Score = LS()

for i in range(1):


    # Reader
    # Convert to all everything
    # Perfect Score : 1:'QC', 2: 'IT', 3: 'TECH', 4: "25 <= X >= 30"
    # 1. Assign Lead Instance
    Lead_Instance = {1:'QC', 2: 'IT', 3: 'TECH', 4: "25 <= X >= 30"}

    # 2. Convert Each Attribute to its corresponding score
    Converted_AttributeValue = Dog_Score.lead_Score_Assignment(Lead_Instance)

    # 3. Compute the Converted Value
    Lead_Score = Dog_Score.lead_Score_Computation(Converted_AttributeValue)

    # Save to database
    print("Lead Score : ", Lead_Score)
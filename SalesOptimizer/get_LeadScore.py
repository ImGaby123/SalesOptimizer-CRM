from models.LeadScoring import LeadScoring as LS
from Data.Lead_Data import Lead_Data
from DB.db_functions import db_functions
from DB.db_connection import db_connection

Dog_Function = db_functions(db_connection())
Dog_Score = LS()
Dog_Data = Lead_Data()


LeadInformation = Dog_Data.getLeadInformation()
#print("Information: ", Information)

LeadCount = len(LeadInformation)
print(LeadCount)

for lead in LeadInformation:

    ID = str(lead[0]).upper()
    Country = lead[1].upper()
    City = lead[2].upper()
    JobTitle = lead[3].upper()
    Industry = lead[4].upper()
    yrsInIndustry = lead[5]


    print(f"ID: {ID}, Country: {Country}, City: {City}, Job Title: {JobTitle}, Industry: {Industry}, Years In Industry: {yrsInIndustry}")

    # Reader
    # Convert to all everything
    # Perfect Score : 1:'QC', 2: 'IT', 3: 'TECH', 4: "25 <= X >= 30"
    # ICP: Country, City, Job Title, Industry, Years in Industry

    # 1. Assign Lead Instance
    Lead_Instance = {1:Country, 2: City, 3: JobTitle, 4:Industry , 5:yrsInIndustry}

    # 2. Convert Each Attribute to its corresponding score
    Converted_AttributeValue = Dog_Score.lead_Score_Assignment(Lead_Instance)

    # 3. Compute the Converted Value
    Lead_Score = Dog_Score.lead_Score_Computation(Converted_AttributeValue)

    # 4. Save to database
    Dog_Function.update_leadScores(lead[0], Lead_Score)
    print("Lead Score : ", Lead_Score)
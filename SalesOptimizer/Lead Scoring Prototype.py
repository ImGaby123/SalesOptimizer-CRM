
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

# This will make the Lead score in the range from 0 to 10



# Variable Assignment Example:
ICP_Attributes = {"X1": {"Dog": 3}, "X2":4, "X3":5}
print(ICP_Attributes["X1"]["Dog"])


# -------------------------- ICP Rule Variables

# ICP Attributes:
# X1 X2 X3 X4
# Exists as it is and definition of such will not be necessary

ICP_Attributes = {
    "X1": {"QC":10, "Manila": 8, "Any":5}, 
    "X2": {"IT": 10, "CS":9,"Any":5}, 
    "X3": {"Techonology":10, "Marketing":8, "Commerce":6, "Any":5},
    "X4": {"25 <= x >= 30": 10, "31 <= x >= 35": 8, "Any": 5}
    }

for i in ICP_Attributes:
    print(f"{i} : {ICP_Attributes[i]}")
    for j in ICP_Attributes[i]:
        print(f"{j} : {ICP_Attributes[i][j]}")

# ICP Weights
Attribute_Weights = {
    "X1": 0.14,
    "X2": 0.29,
    "X3": 0.25,
    "X4": 0.32
    }


# Total Number of Attributes
M = len(ICP_Attributes)

print("M : ",M)


# -------------------------- Individual Customer Scores
Lead_Attributes = {
    "X1" : 10,
    "X2" : 10,
    "X3" : 10,
    "X4" : 5
}

# -------------------------- LS Computation

Lead_Score = []
for n in Lead_Attributes:
    Lead_Score.append(Lead_Attributes[n] * Attribute_Weights[n])

Lead_Score = sum(Lead_Score)

print(Lead_Score)
from pprint import pprint

# Nested dictionary

emps = {
    "Chandu" : {
        "Name" : "Chandu Sharma",
        "Salary" : 15000,
        "Designation" : "foreman"
    },
    "Rohit" : {
        "Name" : "Rohit Kumar",
        "Salary" : 20000,
        "Designation" : "Assistant 1",
        "Manager" : "Ravi Prakash"
    },
    "Faheem" : {
        "Name" : "Fahim Ansari",
        "Salary" : 40000,
        "Designation" : "Data Analyst"
    }
}

pprint(emps) 

print("Designation of Chandu:", emps["Chandu"]["Designation"]) 

for key, data in emps.items():
    print(key, "⏬")
    for k, v in data.items():
        print(k, v)    
    print("- -" * 10) 
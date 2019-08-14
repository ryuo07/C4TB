Name = ["Huy", "Tung", "M.Duc"]
Role = ["Waiter", "Cook", "Manager"]
Hour = [12, 24, 20]
Salary_per_hour = [0.8, 1.5, 2]
l = len(Name)
for i in range(l):
    employee = {
        "Name" : Name[i],
        "Role" : Role[i],
        "Hour" : Hour[i],
        "Salary per hour ($)" : Salary_per_hour[i],
    }
    print("employee",i+1,":",employee)

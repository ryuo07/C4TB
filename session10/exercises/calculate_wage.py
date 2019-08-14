employee = [
    {
        'Name': 'Huy',
        'Role': 'Waiter', 
        'Hour': 12, 
        'Salary per hour ($)': 0.8
    },
    {
        'Name': 'Tung', 
        'Role': 'Cook', 
        'Hour': 24, 
        'Salary per hour ($)': 1.5
    },
    {
        'Name': 'M.Duc', 
        'Role': 'Manager', 
        'Hour': 20, 
        'Salary per hour ($)': 2
    },
    {
        'Name': 'Don', 
        'Role': 'Waiter', 
        'Hour': 12, 
        'Salary per hour ($)': 0.9
    },
    {
        'Name': 'H.Duc', 
        'Role': 'Waiter', 
        'Hour': 14, 
        'Salary per hour ($)': 0.7
    }
]
print(employee)
l = len(employee)
for i in range(l):
    a = employee[i]
    b = a['Name']
    c = a['Salary per hour ($)']
    d = int(a['Hour'])
    e = c*d*30
    print("employee:",b,", salary per month:",e)
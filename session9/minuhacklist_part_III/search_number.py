list = [5, 1, 8, 92, -1, 30]
n = int(input("Enter a Number: "))

if n in list :
    a = list.index(n) + 1
    print("Found, position",a)  
else :
    print("Not found in our list")
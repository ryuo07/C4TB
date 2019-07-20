a = int(input("enter month: "))
if a == 1 or a == 3 or a == 5 or a== 7 or a== 8 or a== 10 or a== 12:
    print("the month you enter has 31 day")
elif a == 2:
    print("the month you enter has 28 day")
else:
    print("the month you enter has 30 day")
while True:
    count = 0
    password = input("enter your password? ")
    b = int(password)
    while (b >0):
        b = b // 10
        count = count +1
    a = count
    print(a)
    print(password)
    if password.isalpha():
        print("invalid password, password must include number")
    elif a <9:
        print("invalid password, password must more than 8 digit ")
    else:
        print("valid password")
        break
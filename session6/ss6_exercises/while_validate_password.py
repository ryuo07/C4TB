while True:
    password = input("enter your password? ")
    print(password)
    if password.isalpha():
        print("invalid password, must include number")
    else:
        print("valid password")
        break
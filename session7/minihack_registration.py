while True:
    a = input("email:")
    if '@' in a and '.' in a:
        print("valid email")
        break
    else:
        print("invalid email, must include @ and . ")
b = input("id:")

while True:
    c = input("password:")
    if c.isalpha():
        print("invalid password, must include number")
    elif c.isdigit():
        print("invalid password, must include alpha")
    else:
        print("valid password")
        break

while True:
    d = input("enter your password again:")
    if c == d :
        print("correct password")
        break
    else:
        print("incorrect password, please enter again")
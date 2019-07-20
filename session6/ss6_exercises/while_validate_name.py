while True:
    name = input("enter your name? ")
    print(name)
    if name.isalpha():
        print("valid name")
        break
    else:
        print("invalid name, include number")
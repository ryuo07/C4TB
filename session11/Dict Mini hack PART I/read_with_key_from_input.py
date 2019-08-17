computers = {
    "HP" : 20,

    "DELL" : 50,

    "MACBOOK" : 12,

    "ASUS" : 30,
}
print(computers)
a = input("enter a type of computer:").upper()
print("number of ", a , computers[a])
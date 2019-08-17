computers = {
    "HP" : 20,

    "DELL" : 50,

    "MACBOOK" : 12,

    "ASUS" : 30,
}
print(computers)
a = input("enter a computer type:").upper()
b = input("enter number of that computer:")
computers[a] = b

print(computers)
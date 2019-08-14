person = {
    "name" : "latina",
    "description" : "cute",
    "species" : "demon",
    "hair color" : "white",
    "age" : 8
}
print(person)
for i in range(2):
    a = input("enter a key you want to change or add more datail:")
    b = input("enter new value for key you just enter:")
    person[a] = b
print(person)
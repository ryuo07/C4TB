person = {
    "name" : "latina",
    "description" : "cute",
    "species" : "demon",
    "hair color" : "white",
    "age" : 8
}
print(person)
a = "name" in person
b = "nationality" in person
if a == True:
    print("key ‘name’ exists in my dictionary")
else:
    print("key ‘name’ does not exist in my dictionary")

if b == True:
    print("key ‘nationality’ exists in my dictionary")
else:
    print("key ‘nationality’ does not exist in my dictionary")


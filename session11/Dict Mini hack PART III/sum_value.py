computers = {
    "HP" : 20,

    "DELL" : 50,

    "MACBOOK" : 12,

    "ASUS" : 30,
}

print(computers)
a = 0

for k,v in computers.items():
    a = a + v
print(a)
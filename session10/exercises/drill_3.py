character1 = {
    "name" : "Latina",
    "gender" : "female",
    "description" : "cute, quick-learning person, clever",
    "species" : "demon",
    "hair color" : "white",
    "age" : 10,
}
character2 = {
    "name" : "Dale",
    "gender" : "male",
    "description" : "friendly, smart, care about other people",
    "species" : "human",
    "hair color" : "brown",
    "age" : 18,
}
character3 = {
    "name" : "Chloe",
    "gender" : "female",
    "description" : "latina best friend, a funny person, alway use fist instead of talk",
    "species" : "human",
    "hair color" : "black",
    "age" : 10,
}
character4 = {
    "name" : "Rudy",
    "gender" : "male",
    "description" : "easy to get angry, weak person, some time really naughty",
    "species" : "human",
    "hair color" : "red",
    "age" : 10,
}
for i in range(2):
    a = input("enter chacracter name:")

    if a == character1["name"]:
        print(character1)
    elif a == character2["name"]:
        print(character2)
    elif a == character3["name"]:
        print(character3)
    elif a == character4["name"]:
        print(character4)
    elif a == "Exit":
        break
    else:
        print("wrong name, please enter again!!!")
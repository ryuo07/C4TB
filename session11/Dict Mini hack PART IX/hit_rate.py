from random import *

character_info = {
    "Name" : "Light",
    "Age" : 17,
    "Strength" : 8,
    "Defense" : 10,
    "HP" : 100,
    "Backpack" : ["Shield", "Bread Loaf"],
    "Gold" : 100,
    "Level" : 2,
}
skills = {
    "Skill 1" : {
        "Name" : "Tackle",
        "Minimum level" : 1,
        "Damage" : 5,
        "Hit rate" : 0.3,
},

"Skill 2":{
        "Name" : "Quick attack",
        "Minimum level" : 2,
        "Damage" : 3,
        "Hit rate" : 0.5,
},


"Skill 3": {
        "Name" : "Strong Kick",
        "Minimum level" : 4,
        "Damage" : 9,
        "Hit rate" : 0.2,
}
}
a = 1

character_info = {
    "Name" : "Light",
    "Age" : 17,
    "Strength" : 8,
    "Defense" : 10,
    "HP" : 100,
    "Backpack" : ["Shield", "Bread Loaf"],
    "Gold" : 100,
    "Level" : 2,
}
skills = {
    "Skill 1" : {
        "Name" : "Tackle",
        "Minimum level" : 1,
        "Damage" : 5,
        "Hit rate" : 0.3,
},

"Skill 2":{
        "Name" : "Quick attack",
        "Minimum level" : 2,
        "Damage" : 3,
        "Hit rate" : 0.5,
},


"Skill 3": {
        "Name" : "Strong Kick",
        "Minimum level" : 4,
        "Damage" : 9,
        "Hit rate" : 0.2,
}
}
a = 1

print("Character skills:")
for k,v in skills.items():
    print(a,")",skills[k]["Name"])
    a = a + 1
while True:
    b = int(input("enter skill number you want to use:"))
    c = random()
    print("hit rate:",c)
   
    if b == 1:
        print("choosing skill:", skills["Skill 1"]["Name"])
        if skills["Skill 1"]["Minimum level"] > character_info["Level"]:
            print("unable to use skill, your level is not enough")
        elif skills["Skill 1"]["Hit rate"] > c:
            print("skill miss, not close enough")
        else:
            print(skills["Skill 1"]["Name"])
            print("Damage deal:",skills["Skill 1"]["Damage"])
    if b == 2:
        print("choosing skill:", skills["Skill 2"]["Name"])
        if skills["Skill 2"]["Minimum level"] > character_info["Level"]:
            print("unable to use this skill, your level is not enough")
        elif skills["Skill 2"]["Hit rate"] > c:
            print("skill miss, not close enough")
        else:
            print(skills["Skill 2"]["Name"])
            print("Damage deal:",skills["Skill 2"]["Damage"])
    if b == 3:
        print("choosing skill:", skills["Skill 3"]["Name"])
        if skills["Skill 3"]["Minimum level"] > character_info["Level"]:
            print("unable to use this skill, your level is not enough")
        elif skills["Skill 3"]["Hit rate"] > c:
            print("skill miss, not close enough")
        else:
            print(skills["Skill 3"]["Name"])
            print("Damage deal:",skills["Skill 3"]["Damage"])



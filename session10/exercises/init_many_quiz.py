count = 0


question = "ranking of the vn team in PUBG Nations Cup Seoul 2019:"
print(question)
answers = {
    "a)" : "first place",
    "b)" : "second place",
    "c)" : "third place",
    "d)" : "fouth place",
}

for k,v in answers.items():
    print(k,v)
a = input("enter your answer:")
if a == "a" or a == "b" or a == "c" :
    print("Not a correct answer :( , please try again!!! ")
elif a == "d":
    print("correct !!!!")
    count = count + 1
    
question = "Who is the coach of Vietnam team in this tournament?:"
print(question)
answers = {
    "a)" : "Độ Mixi",
    "b)" : "DJ Chip",
    "c)" : "Xemesis",
    "d)" : "Pew Pew",
}

for k,v in answers.items():
    print(k,v)
a = input("enter your answer:")
if a == "a" or a == "d" or a == "c" :
    print("Not a correct answer :( , please try again!!! ")
elif a == "b":
    print("correct !!!!")
    count = count + 1

print("Result:")
print("correct answer:", count)
print("percent of questions answered correctly:", count/2*100, "%")
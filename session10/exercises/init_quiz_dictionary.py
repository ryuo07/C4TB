question = "How many eggs a cat laid per year:"
print(question)
answers = {
    "a)" : "ten",
    "b)" : "zero",
    "c)" : "one billion",
    "d)" : "i don't know",
}

for k,v in answers.items():
    print(k,v)
x = 0
while True:
    a = input("enter your answer:")
    if a == "a" or a == "c" :
        print("Not a correct answer :( , please try again!!! ")
    elif a == "d":
        print("what were you thinking about??? Please use your brain !!!")
    elif a == "b":
        print("wow!!! you are realy smart!!!")
        break
    x = x + 1
    if x >= 5:
        print("you have answered wrong 5 times, why you keep choosing the wrong answer? WHY? WHY?")
        print("this is not a joke, please choose b!!!")
    
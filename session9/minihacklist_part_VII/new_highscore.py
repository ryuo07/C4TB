highscore = [45, 67, 56, 78]
for a,b in enumerate(highscore):
    print(a+1,b, sep=".")
c = int(input("enter your new highscore:"))
highscore.append(c)
for a,b in enumerate(highscore):
    print(a+1,b, sep=".")
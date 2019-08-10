highscore = [45, 67, 56, 78]
highscore.sort(reverse=True)
for a,b in enumerate(highscore):
    print(a+1,b, sep=".")
c = int(input("enter your new highscore:"))
highscore.append(c)
highscore.sort(reverse=True)
for a,b in enumerate(highscore):
    print(a+1,b, sep=".")
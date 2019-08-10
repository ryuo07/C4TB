highscore = [45, 67, 56, 78]
for i in range(2):    
    highscore.sort(reverse=True)
    l = len(highscore)
    print("high score:")
    if l<=5:
        l = l
    elif l>5:
        l = 5
    for i in range(l):
        print(i+1,highscore[i], sep=".")
    c = int(input("enter your new highscore:"))
    highscore.append(c)
    highscore.sort(reverse=True)
    l = len(highscore)
    print("new high score:")
    if l<=5:
        l = l
    elif l>5:
        l = 5
    for i in range(5):
        print(i+1,highscore[i], sep=".")
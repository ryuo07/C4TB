list = [5, 1, 8, 92, 7, 30]
l = len(list)
for i in range(l):
    b = list[i]
    c = b%2
    if c==0:
        print(b)
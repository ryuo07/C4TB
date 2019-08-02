a = input("favorite things:")
b = a.split(',')
print(*b, sep=',')
l = len(b)
for c in range(l):
    print(b[c])
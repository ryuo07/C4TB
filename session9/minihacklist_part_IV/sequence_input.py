a = input("Enter a list of numbers, separated by ‘,’:")
list = a.split(',')
l = len(list)
d = []
for i in range(l):
    b = int(list[i])
    c = b%2
    if c==0:
        d.append(b)

print("All even numbers from entered list:")
print(*d, sep=",")

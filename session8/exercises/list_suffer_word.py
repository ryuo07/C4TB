a = input('enter a word: ')
b = list(a)
l = len(a)
for i in range(l):
    from random import randrange
    c = randrange(l)
    l = l-1
    print(b[c])
    b.pop(c)
    

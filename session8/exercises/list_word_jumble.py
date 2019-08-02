words = ['cat', 'dog', 'rabbit', 'bird', 'chicken', 'duck', 'fish', 'mouse', 'elephant', 'penguin', 'turtle', 'cow', 'goat', 'sheep', 'horse', 'raven', 'swan', 'owl', 'lion', 'panda', 'kangaroo', 'leopard', 'fox']
while True:
    from random import randrange
    x = randrange(23)
    a = words[x]
    b = list(a)
    l = len(a)
    word = []
    for i in range(l):
        from random import randrange
        c = randrange(l)
        l = l-1
        word.append(b[c])
        b.pop(c)
    print(*word)
    d = input("enter word after rearrange:")

    if d == a:
        print("correct")
    else:
        print("incorrect")
        break
    
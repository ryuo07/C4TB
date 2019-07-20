while True:
    from random import randrange
    a = randrange(20)
    print("a=")
    print(a)
    b = randrange(20)
    print("b=") 
    print(b)
    c = a-b
    d = a+b
    e = randrange(-20,40)
    from random import randint
    f = randint(0,2)
    if f == 0:
        print("a+b=")
    elif f == 1:
        print("a-b=")
    print(e)
    g = input("enter correct or incorrect:")
    h = "correct"
    i = "incorrect"
    if g == h and e == c or g==h and e == d:
        print("correct, next question:")
    elif g == i and e!= c or g==i and e != d:
        print("correct, next quettion:")
    else:
        print("game over")
        break
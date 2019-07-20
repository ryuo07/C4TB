x = int(input("enter a number: "))
c = x%2
if c==0:
    b = range( x-1, 0, -2)
    print(*b)
elif c==1:
    b = range( x, 0, -2)
    print(*b)
else:
    print("not a number")
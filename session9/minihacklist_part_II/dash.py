from turtle import *

colors = ["yellow","red","blue","green"]
for i in range(10):
    if i%4 == 0:
        color("yellow")
        begin_fill()
        forward(50)
        end_fill()
    elif i%4 == 1:
        color("red")
        begin_fill()
        forward(50)
        end_fill()
    elif i%4 ==2:
        color("blue")
        begin_fill()
        forward(50)
        end_fill()
    elif i%4 ==3:
        color("green")
        begin_fill()
        forward(50)
        end_fill()


mainloop()
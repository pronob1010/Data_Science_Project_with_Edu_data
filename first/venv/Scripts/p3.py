year = 2000;
if year % 4!=0:
    print("no")
else:
    if year%100 == 0:
        if year%400 == 0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")


import turtle

turtle.shape("turtle")

turtle.forward(150)
turtle.left(45*3)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

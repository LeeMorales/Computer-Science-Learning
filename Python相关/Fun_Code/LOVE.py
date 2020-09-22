import turtle

turtle.bgcolor("black")
turtle.pensize(2)
sizeh = 1.2


def curve():
    for ii in range(200):
        turtle.right(1)
        turtle.forward(1 * sizeh)


def break_line(right, length):
    if right:
        turtle.right(100)
    else:
        turtle.left(100)

    turtle.forward(length * sizeh)


turtle.speed(1000)
turtle.color("red", "pink")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65 * sizeh)
curve()
turtle.left(120)
curve()
turtle.forward(111.65 * sizeh)

# FFF
turtle.right(170)
turtle.forward(50 * sizeh)

break_line(False, 50)
break_line(True, 50)

break_line(False, 50)
break_line(True, 30)

# Turn Back
turtle.right(80)
turtle.forward(10 * sizeh)

break_line(True, 20)
break_line(False, 50)

break_line(True, 50)
break_line(False, 50)

turtle.end_fill()
turtle.hideturtle()

input("Waiting for exit")
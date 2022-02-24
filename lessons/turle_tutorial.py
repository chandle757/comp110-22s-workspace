from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)
s: float = 100
i: int = 0
b: int = 0

leo.pencolor("black")
leo.fillcolor(0, 0, 0)

leo.penup()
leo.goto(0, 0)
leo.pendown()
leo.begin_fill()
while (i < 9):
    leo.forward(s)
    leo.right(40)
    i += 1
leo.end_fill()
done()

import turtle

screen = turtle.screen()
screen.screensize(400,400)
screen.title("star")
screen.bgcolor("blue")

t = turtle.Turtle()
t.color("orange")
t.width(3)

n = 3
a = 360/n

for i in range(n):
    t.forward(100)
    t.left(a)

t.left(90)
t.penup()
t.forward(65)
t.right(90)
t.pendown()

for i in range(n):
    t.forward(100)
    t.right(a)

turtle.done()
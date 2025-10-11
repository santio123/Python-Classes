import turtle

screen = turtle.screen()
screen.screensize(400,400)
screen.title("polygon")
screen.bgcolor("blue")

t = turtle.Turtle()
t.color('orange')
t.width(10)
t.fillcolor('green')
n = 4
a = 360/4
t.begin_fill()
for i in range(4):
    t.forward(180)
    t.right(a)
t.end_fill()

turtle.done()
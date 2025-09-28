import turtle

screen = turtle.screen()
screen.screensize(400,400)
screen.title("polygon")
screen.bgcolor("blue")

t = turtle.Turtle()
t.color('orange')
t.width(10)
t.fillcolor('green')
n = 6
a = 360/6
t.begin_fill()
for i in range(6):
    t.forward(150)
    t.right(a)
t.end_fill()

turtle.done()
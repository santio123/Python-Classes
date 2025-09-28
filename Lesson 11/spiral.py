import turtle

screen = turtle.screen()
screen.screensize(400,400)
screen.title("spiral square")
screen.bgcolor("blue")

t = turtle.Turtle()
t.color("orange")
t.width(1)

s = 5
while True:
    t.forward(s)
    t.right(90)
    s += 3
import turtle

t = turtle.Turtle()
t.pensize(4)
turtle.bgcolor("pink")

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.pencolor("black")
t.fillcolor("white")
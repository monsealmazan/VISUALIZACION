import turtle

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.speed(1)
t.hideturtle()
t.goto(0,-10)


t.pensize(5)
t.color("red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()


t.penup()
t.goto(-90,130)
t.pendown()
t.color("white")
t.write("te amo muchoo", font=("verdana",20,"bold"))

t.penup()
t.goto(-50,90)
t.pendown()
t.color("white")
t.write("mi vida ", font=("verdana",10,"bold"))
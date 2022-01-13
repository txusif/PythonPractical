import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(2)
t.speed('fastest')

col = ('orange', 'red', 'pink')
for i in range(100):
    t.pencolor(col[i%3])
    t.forward(i*6)
    t.right(120)

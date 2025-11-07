import turtle
t = turtle.Pen()
#1번째 서클
t.penup()
t.goto(-200,0)
t.pendown()
t.circle(100)
t.circle(50)

#2번째 서클
t.penup()
t.goto(0,0)
t.pendown()
t.circle(100)
t.circle(50)

#3번째 서클
t.penup()
t.goto(200,0)
t.pendown()
t.circle(100)
t.circle(50)

turtle.done()
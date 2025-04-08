import turtle

myT = turtle.Turtle()
myT.shape('turtle')

mySpeed = int(input('주행 속도 측정기: '))

positions = [-120, 0, 120]  
colors = ["red", "yellow", "green"]


for pos in positions:
    t.up()
    t.goto(pos, 0)
    t.down()
    t.circle(50)


if mySpeed <= 50:
    fill_index = 2 
elif 50 < mySpeed <= 60:
    fill_index = 1  
else:
    fill_index = 0  

# 색칠하기
t.up()
t.goto(positions[fill_index], 0)
t.down()
t.fillcolor(colors[fill_index])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()

t.hideturtle()
turtle.done()
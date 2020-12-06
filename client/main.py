import turtle
import time
import json
import requests




lastx = 0
lasty = 0
playerid = 1
wn = turtle.Screen()
wn.bgcolor("white")
player = turtle.Turtle()
player.color("black")
player.shape("triangle")
speed = 0
player.penup()
turtle.listen()
wn.title(playerid)
#empty other players
player2 = turtle.Turtle()
player2.color("red")
player2.shape("triangle")
player2.penup()


#starting point
player.hideturtle()
player.goto(155, -20)
player.showturtle()
player.setheading(90)

player2.hideturtle()
player2.goto(190, -20)
player2.showturtle()
player2.setheading(90)

#borders
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-175, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(8):
    mypen.forward(250)
    mypen.left(45)
mypen.hideturtle()

mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-125, -175)
mypen.pendown()
mypen.pensize(3)
for side in range(8):
    mypen.forward(150)
    mypen.left(45)
mypen.hideturtle()
#starting line
mypen = turtle.Turtle()
mypen.up()
mypen.setposition(131, 0)
mypen.pendown()
mypen.pensize(3)
for side in range(1):
    mypen.forward(120)
mypen.hideturtle()




#definitions
def turnleft():
    player.left(15)
def turnright():
    player.right(15)
def increasespeed():
    global speed
    speed += 1
def decreasespeed():
    global speed
    speed-= 1

#controls
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")





#speed
if playerid == 1:
    url = 'http://localhost:3000/ptwo'
if playerid == 2:
    url = 'http://localhost:3000/pone'
while True:

    player.forward(speed)


    ppos = player.pos()
    if ppos[0] != lastx and ppos[0] != lasty:
        x = {
            'id': playerid,
            'x': ppos[0],
            'y': ppos[1]
        }
        r = requests.post('http://localhost:3000/api', data=x)
    p2s = requests.get(url)
    pythonsucks = p2s.text
    p2a = pythonsucks.split(",")
    p2a[0] = p2a[0].replace('"', '')
    p2a[0] = p2a[0].replace('[', '')
    p2a[1] = p2a[1].replace('"', '')
    p2a[1] = p2a[1].replace(']', '')
    player2.setpos(float(p2a[0]), float(p2a[1]))
    lastx = ppos[0]
    lasty = ppos[1]
    time.sleep(0.1)

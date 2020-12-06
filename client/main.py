import requests

url = 'http://localhost:3000/api'

i = input("what is ur name: ");
correct_payload = {'i': i}

r = requests.post(url, data=correct_payload)
print(r.text)

import turtle

#screen and player
wn = turtle.Screen()
wn.bgcolor("white")
player = turtle.Turtle()
player.color("black")
player.shape("triangle")
speed = 0
player.penup()
turtle.listen()
player2 = turtle.Turtle()
player2.color("red")
player2.shape("triangle")

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
while True:
    player.forward(speed)

from turtle import *
import random

iterations = 1000

lineWidth = 5

dist = 5
angle = 89

colorNames = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]

speed(0)

for i in range(iterations):
    #Set color of next line
    rand = random.randint(1, len(colorNames))
    #color(colorNames[rand - 1])
    color(colorNames[i % len(colorNames)])

    #Thickness of next line
    width(lineWidth)

    #Draw Distance of line
    randDistance = random.randint(0, 200)
    forward(dist * i)

    #drawing angle of next line
    randAngle = random.randint(0, 360)
    left(angle)

done()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:46:02 2020

@author: mckenzieporteous
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Mckenzieporteous
Author: Mckenzieporteous
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t = Turtle()
t.pensize(100)


#n = int(input'10')
#1 = int(input'100')
 up()

left(90)

forward(100)

left(90)

forward(100)

forward(50)

forward(50)

down()

color('orange')

dot(50)

dot(100)

color('pink')

dot(50)

up()

color('green')

left(180)

forward(200)
forward(200)

right(90)

forward(100)

color('light blue')

down()

dot(200)

color('light yellow')

dot(100)

up()

forward(50)

forward(100)

left(90)

backward(300)

color('light green')

backward(20)

down()

dot(150)

color('green')

dot(75)

home()

backward(100)

backward(75)

backward(20)

color('purple')

left(180)

left(90)

forward(50)

forward(50)

up()

left(90)

color('light yellow')

forward(100)

forward(75)

color('pink')

up()

home()

down()

color(236, 173, 255)

forward(300)

left(90)

forward(50)

forward(50)

shape('triangle')

dot(30)

up()

right(90)

color(173, 194, 255)

dot(20)

shape('square')

up()

forward(90)

color(173, 255, 221)

down()

right(90)

forward(40)

up()

left(90)

forward(30)

left(90)

down()

forward(40)

up()

home()

shape('classic')

goto(100,-100)

down()

color('white')

forward(50)

goto(150,-150)

goto(130,-200)

goto(110,-150)

goto(100,-100)

up()

goto(0,200)

down()

goto(-50,250)

left(90)

goto(-50,300)

forward(20)

goto(0,350)

goto(50,300)

backward(60)

goto(0,200)

color('red')

up()

left(90)

forward(200)

forward(100)

left(90)

forward(300)

down()

forward(100)

backward(400)
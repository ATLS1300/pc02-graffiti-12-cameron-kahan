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

#!/usr/bin/python
"""Think Like a Scientist: Excerise 4.3

"""
from __future__ import division
import math
from swampy.TurtleWorld import *

world =  TurtleWorld()
bob = Turtle()
print bob

def polyline(t, n, length, angle):
	r= length//(2*math.sin(3.14/n))
	for i in range(n):
		fd(t, length)
		lt(t, (180+angle)/2)
		fd(t,r)
		lt(t,180)
		fd(t,r)
		lt(t, (180+angle)/2)



polyline(bob, 5, 100, 360/5)


bob.delay = 0.000001

arc(bob,100,60)
wait_for_user()
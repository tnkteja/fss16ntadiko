#!/usr/bin/python
"""Think Like a Scientist: Excerise 4.3

"""
from __future__ import division
from swampy.TurtleWorld import *

world =  TurtleWorld()
bob = Turtle()
print bob

def square(t,l):
	for i in range(4):
		fd(bob, l)
		lt(bob)

def polygon(t,n,l):
	for i in range(n):
		fd(bob, l)
		lt(bob,360/n)

def circle(t,r):
	t.delay = 0.01

	polygon(t, 100, (2*3.14*r)/100)

circle(bob,100)
wait_for_user()
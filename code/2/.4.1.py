#!/usr/bin/python
"""Think Like a Scientist: Excerise 4.3

"""
from swampy.TurtleWorld import *

world =  TurtleWorld()
bob = Turtle()
print bob

def square(t):
	for i in range(4):
		fd(bob, 100)
		lt(bob)

square(bob)
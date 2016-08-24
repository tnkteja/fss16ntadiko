#!/usr/bin/python
"""Think Like a Scientist: Excerise 4.3

"""
from swampy.TurtleWorld import *

world =  TurtleWorld()
bob = Turtle()
print bob

def square(t,l):
	for i in range(4):
		fd(bob, l)
		lt(bob)


for i in range(0,100,10):
	square(bob,i)

wait_for_user()
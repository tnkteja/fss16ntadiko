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

def arc(t,r,a):
	t.delay = 0.0001
	n=10000
	for i in range(a*n//360):
		fd(bob, (2*3.14*r)/n)
		lt(bob,360/n)
	lt(bob,90)
	fd(bob,r)
	lt(bob,180-a)
	fd(bob,r)

arc(bob,100,60)
wait_for_user()
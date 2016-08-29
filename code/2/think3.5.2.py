#!/usr/bin/python
"""Think Python : How To Think Like A Computer Scientist: Excercise 3.5

Exercise 5  
2. Write a function that draws a similar grid with four rows and four columns.
"""

def grid(r,c):
	for i in range(r):
		print ''.join(['+']+[ 4*'-'+'+' for j in range(c)])
		for k in range(4):
			print ''.join(['|']+[ 4*' '+'|' for j in range(c)])
	print ''.join(['+']+[ 4*'-'+'+' for j in range(c)])

grid(4,4)
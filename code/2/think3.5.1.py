#!/usr/bin/python
"""Think Like A Computer Scientist: Excercise 3.5

Exercise 5  
1. This exercise can be done using only the statements and other features we have learned so far.
Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence:
print '+', '-'
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.
print '+', 
print '-'
The output of these statements is '+ -'.
A print statement all by itself ends the current line and goes to the next line.

Write a function that draws a similar grid with four rows and four columns.
"""

def grid(r,c):
	for i in range(r):
		print ''.join(['+']+[ 4*'-'+'+' for j in range(c)])
		for k in range(4):
			print ''.join(['|']+[ 4*' '+'|' for j in range(c)])
	print ''.join(['+']+[ 4*'-'+'+' for j in range(c)])

grid(2,2)
#!/usr/bin/python
"""Think Like A Computer Scientist: Excercise 3.4

	Exercise 4  
	A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:
	def do_twice(f):
	    f()
	    f()
	Here's an example that uses do_twice to call a function named print_spam twice.
	def print_spam():
	    print 'spam'

	do_twice(print_spam)
	
	Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

"""

def do_twice(f,v):
	f(v)
	f(v)

def print_spam(v):
	print v
	print v

def do_four(f,v):
	do_twice(f, v)
	do_twice(f, v)

do_four(print_spam, "spam")
#!/usr/bin/python
"""Think Python: How to Think Like A Computer Scientist: Excercise 3.4

	Exercise 4  
	A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:
	def do_twice(f):
	    f()
	    f()
	Here's an example that uses do_twice to call a function named print_spam twice.
	def print_spam():
	    print 'spam'

	do_twice(print_spam)
	1.Type this example into a script and test it.
"""

def do_twice(f):
	f()
	f()

def print_spam():
	print "spam"

do_twice(print_spam)
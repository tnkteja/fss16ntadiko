#!/usr/bin/python
"""Think Python : How To Like a Computer Scientist: Excercise 3.1


	def print_lyrics():
	    print "I'm a lumberjack, and I'm okay."
	    print "I sleep all night and I work all day."

	repeat_lyrics()

	def repeat_lyrics():
	    print_lyrics()
	    print_lyrics()


Exercise 2  
Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?
"""

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()

#!/usr/bin/python
"""Think Like a Computer Scientist: Excercise 3.1


	def print_lyrics():
	    print "I'm a lumberjack, and I'm okay."
	    print "I sleep all night and I work all day."

	def repeat_lyrics():
	    print_lyrics()
	    print_lyrics()

repeat_lyrics()

Exercise 1  
Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.

"""

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

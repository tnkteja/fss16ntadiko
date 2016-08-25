# Homework 2

## Active Shooter Training Excercise

### List two things not to do during an active shooter event.

1. When the law enforcement officiers arrive, don't point at them , don't scream or yell, and don't be loud and non-compliant.

2. When among groups in a hiding location, don't stay close to each other but spread out.

### List two things best to do during an active shooter event.

1. If you can get out to a safer place, then get out and call authorities to let them know where you are and whats going on.

2. If you can't get out find a hide out location, blockade the door, switchoff the mobiles and other gadgets.  

## Review-1
### Theory
1. What does a python function return by default?

	Answer: None, if you need something, you need to return it using return statement.

2. How do you access global variables in python?

	Answer: Using the keyword `global` which enforces global scope to the local varibles with corresponding globals.

3. What is a decorator?

	Answer: It is a type annotation, analogous to annotations in Java language. When define a decorator in python for a function or method, it takes the function of the method as argument executes the decorator method and assigns the resulting output to the function name which passed in as the argument.

4. What does a seed do in a random number generator?

	Answer: 

5. What happens if an assertion is false?

	Answer: An exception is thrown with the assert commment as the Error in the console.

##Practice

1. For each of the following, can you offer a 3 line code snippet to demo the idea?
  * Classes

  	Answer: 
  	```

  	```
  * Functions
  * default params
  * variable lists args
  * variable dictionary args
  * decorators
  * exception handling
  
  	Answer:
  	```python
  	try:
  		1/0
  	except ZeroDivisionError as zde:
  		print zde
  	```
2. Write a function that takes 2 args(Arg1 and Arg2) such that Arg 1 is a list of numbers, Arg2 is a number. Return a list of size Arg2 from Arg1 such that no duplicates are present.

	Answer:
	```python
	def func(arg1,arg2):
		return list(set(arg1))[:arg2]
	```
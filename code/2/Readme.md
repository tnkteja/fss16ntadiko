# Homework2

## Active Shooter Excercise

[Answers](https://github.com/tnkteja/fss16ntadiko/tree/hw2/etc/2)

## Introductory Python

The source files are self explanatory.

##### 3.1  
code:
[think3.1.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.1.py) 

Results:

![alt think3.1.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.1.png)

##### 3.2
code:
[think3.2.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.2.py) 

Results:

![alt think3.2.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.2.png)

##### 3.3  
code:
[think3.3.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.3.py) 

Results:

![alt think3.3.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.3.png)

##### 3.4
| Code | Results |
|:----:|:-------:|
|[think3.4.1.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.4.1.py)|![alt think3.4.1.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.4.1.png)|
|[think3.4.2.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.4.2.py)| N/A|
|[think3.4.3.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.4.3.py)| N/A|
|[think3.4.4.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.4.4.py)|![alt think3.4.4.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.4.4.png)|
|[think3.4.5.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.4.5.py)|![alt think3.4.5.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.4.5.png)|

##### 3.5
|Code|Results|
|:--:|:------:|
|[think3.5.1.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.1.py)|![alt think3.5.1.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.5.1.png)|
|[think3.5.2.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.2.py)|![alt think3.5.2.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/3.5.2.png)||

#### 4.2

|Code|Results|
|:--:|:------:|
|[think4.2.a.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.1.py)|![alt think3.5.1.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/think/_2.a.png)|
|[think4.2.b.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.2.py)|![alt think3.5.2.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/think/_2.b.png)||
|[think4.2.c.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.2.py)|![alt think3.5.2.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/think/_2.c.png)||

#### 4.3

|Code|Results|
|:--:|:------:|
|[think4.3.a.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.1.py)|![alt think3.5.1.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/think/_3.a.png)|
|[think4.3.b.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.2.py)|![alt think3.5.2.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/think/_3.b.png)||
|[think4.3.c.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/think3.5.2.py)|![alt think3.5.2.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/think/_3.c.png)||

## Review-1
### Theory
1. What does a python function return by default?

	Answer: None, if you need something, you need to return it using return statement.

2. How do you access global variables in python?

	Answer: Using the keyword `global` which enforces global scope to the local varibles with corresponding globals.

3. What is a decorator?

	Answer: It is a type annotation, analogous to annotations in Java language. When define a decorator in python for a function or method, it takes the function of the method as argument executes the decorator method and assigns the resulting output to the function name which passed in as the argument.

4. What does a seed do in a random number generator?

	Answer: When debugging code using radom number generators, it is often necessary that the sequence produced by the random number generators be same each time we debug.

5. What happens if an assertion is false?

	Answer: An exception is thrown with the assert commment as the Error in the console.

##Practice

1. 3 line code snippet demos

  * Classes

  	Answer: 
  	```python
  	class newClass(object):
  		"""docstring for newClass"""
  		def __init__(self, arg):
  			super(newClass, self).__init__()
  			self.arg = arg

  	print newClass(None)
  	```
  * Functions

  	Answer:
  	```python
  	def function():
  		"""docstring for function"""
  		return None

  	print function()	
  	```
  * default params

  	Answer:
  	```python
	  def defaultParams(defaultParam1=True):
	  	"""docString for function"""
	  	return defaultParam1

	  print defaultParams()
	```
  * variable lists args

  	Answer:
  	```python
  	def variableListsArgs(*arr):
  		"""docString for function"""
  		return arr

  	print isinstance(variableListsArgs(1,2,"3",None),tuple)
  	```

  * variable dictionary args

  	Answers:
  	```python
  	def variableDictionaryArgs(**dic):
  		"""docString for function""""
  		return dic

  	print isinstance(variableDictionaryArgs(arg1="value1",arg2="value2"),dict)
  	```

  * decorators

	Answers:
	```python
	def decorator(f):
		"""docString for function"""
		print f.__name__,"decorated"
		return f

	@decorator
	def func():
		pass
	```

  * exception handling
  
  	Answer:
  	```python
  	try:
  		1/0
  	except ZeroDivisionError as zde:
  		print zde
  	```
 
 code: [practice1.py](https://github.com/tnkteja/fss16ntadiko/blob/hw2/code/2/practice1.py)
  
 Results:

 ![alt practice1.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/p1.png)

2. 

	Answer:
	```python
	import random
	from collections import Counter

	def func(arg1,arg2):
		return list(set(arg1))[:arg2]

	arg1=random.sample(range(1,20)*2,10)
	print func(random.sample(arg1, 9),4)
	```

	code: [practice2.py]()
	
	Results:

	![alt practice2.py](https://rawgit.com/tnkteja/fss16ntadiko/hw2/code/2/.images/p2.png)
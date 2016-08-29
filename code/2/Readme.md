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
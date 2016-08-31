#Homework3 : coding homework


## Review-2

### Practice

#### 1. Iterators

1a. The 
```python
return n
```
statement is at wrong time.
```python
yield n
```
should be there.  Like this
```python
def countdown(n):
   while n >= 0:
     n -= 1
   return  n # fixed

print("We are go for launch")
for x in countdown(10):
   print(x)
print("lift off!")
```
1b.
1c. 
1d. 
1e. 
1f. 
```python
import random

x = []
random.seed(1)
for _ in range(20):
	x.append(random.random())

print(x)
```
1.g  Without `yield`
```python
print xrange(1,1000,2)
```
with yield
```python
```

2a.
*  `__init__`
*  `__setitem__` 

2b. Holder of all the name value pairs for the object of class o. 
2c. 
2d. 

#### 3. 8 Queens
You've seen the knightstour. Can you code up the 8 queens problem in python? (https://en.wikipedia.org/wiki/Eight_queens_puzzle)

#### 4. FSM
What is a finite state machine?
Can you describe an fsm in python for the following problem.
Your in a bar.
 1. You start of sober.
 2. If you are sober you take a drink
 3. If You take a drink then there is a 80% of the time you get drunk and there is a 20% chance you pass out.
 4. If you do not take a drink, there is a 50% chance you get sober.
 5. If you pass out the machine stops

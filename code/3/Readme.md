#Homework3 : coding homework

* 10.15.8 

    Code : [10.15.8.py](https://github.com/tnkteja/fss16ntadiko/blob/hw3/code/3/10.15.8.py)

    Results :

    ![alt 10.15.8.py](https://rawgit.com/tnkteja/fss16ntadiko/hw3/code/3/.images/10.15.8.png)

* Employee Class
    ```python
    class Pretty(object):
        def __repr__(self):
            return self.__class__.__name__ + '( ' + ', '.join([str(k) + " = " + 
                      str(self.__dict__[k]) for k in sorted(self.__dict__.keys())]) +' )'


    class Employee(Pretty):
        """Employee Class"""

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __lt__(self,other):
        	return self.age < other.age
    ```

    Code : [employee.py](https://github.com/tnkteja/fss16ntadiko/blob/hw3/code/3/employee.py)

    Results :

    ![alt employee.py](https://rawgit.com/tnkteja/fss16ntadiko/hw3/code/3/.images/employee.png)

* 18.12.6 [1-6]

    Code : [PokerHand.py](https://github.com/tnkteja/fss16ntadiko/blob/hw3/code/3/PokerHand.py)

    Results :

    ![alt PokerHand.py](https://rawgit.com/tnkteja/fss16ntadiko/hw3/code/3/.images/pokerhand.png)
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
```python
def items(x, depth=-1):
  if isinstance(x,(list,tuple)):
    for y in x:
      for z in items(y, depth+1):
        yield z
  else:
    yield x

def final():
  out=[]
  for x in items([
                    10,
                    [ 20,30],
                    40,
                    [
                      (  50,60,70),
                      [80,90,100],
                      110
                    ]
                  ]):
    if x > 20:
      out+=[x]
  return out
  ```
1c. 
```python
def items(x, depth=-1):
  if isinstance(x,(list,tuple)):
    for y in x:
      for z in items(y, depth+1):
        yield z
  else:
    yield x

def final():
  return [x for x in items([
                    10,
                    [ 20,30],
                    40,
                    [
                      (  50,60,70),
                      [80,90,100],
                      110
                    ]
                  ]) if x > 20]
```
1d.

```python
import string
def non_whitespace(strin):
  return ''.join([ l for l in strin if l not in string.whitespace])

print non_whitespace("sfvsf rg rG\n w wwfwrg \t")  # improve test case here
```

1e.

```python
def lines(string):
  tmp=''
  for ch in string: 
    if ch == "\n":
      yield tmp
      tmp = ''
    else:
      tmp += ch 
  if tmp:
    yield tmp

def strings(string):
  return [ line for line in lines(string) if len(line) > 20]
```

1f. 
```python
import random

x = []
random.seed(1)
for _ in range(20):
	x.append(random.random())

print(x)
```
1.g  

Without `yield`
```python
print xrange(1,1000,2)
```
with yield
```python
def odd():
  n=-1;
  while n<1000:  
      n+=2;
      yield n
```
  Results:

  ![alt practice1](https://rawgit.com/tnkteja/fss16ntadiko/hw3/code/3/.images/practice1.png)
2a.
*  `__init__`
*  `__setitem__` 
* `__getitem__`
* `__repr__`
* `__dict__`

2b. Holder of all the name value pairs (attributes) for the object of class o. 

2c. 

Results :

![alt practice2.c.png](https://rawgit.com/tnkteja/fss16ntadiko/hw3/code/3/.images/practice2.c.png)

2d. 
The object of a Some class appends a value to 8 times and with some probablity, which depends on the number of elements already added and the attempt number, adds the value to random position for later onwards.

Results

![alt practice2.d.png](https://rawgit.com/tnkteja/fss16ntadiko/hw3/code/3/.images/practice2.d.png)

3. 8 Queens

4. FSM
What is a finite state machine?
    
    Code : [practice4.py](https://github.com/tnkteja/fss16ntadiko/blob/hw3/code/3/practice4.py)

    Results : 

    ![alt practice.py](https://rawgit.com/tnkteja/fss16ntadiko/hw3/code/3/.images/practice4.png)
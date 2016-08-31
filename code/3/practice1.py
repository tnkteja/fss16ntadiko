# a.
def countdown(n):
   while n >= 0:
   	yield n
   	n -= 1

print("We are go for launch")
for x in countdown(10):
   print(x)
print("lift off!")

# b.

def items(x, depth=-1):
  if isinstance(x,(list,tuple)):
    for y in x:
      for z in items(y, depth+1):
        yield z
  else:
  	yield _,x

def final():
  out = []
  for _,x in items(  [10,[ 20,30],
                        40,
                        [   (  50,60,70),
                            [  80,90,100],110]]):
   out += [x]
   return out

#print final()

# c.

# d.

import string
def non_whitespace(strin):
	return ''.join([ l for l in strin if l not in string.whitespace])

print non_whitespace("sfvsf rg rG\n w wwfwrg \t")  # improve test case here

#e.

#f.

import random
x = []
random.seed(1)
for _ in range(20):
 x.append(random.random())
print(x)

#g.1


#g.2

print ', '.join(map(str,list(xrange(1,1000,2))))
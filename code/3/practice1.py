def results(q):
  print "="*10,q,"="*10

# a.
def countdown(n):
   while n >= 0:
   	yield n
   	n -= 1

results('a')
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
results('b')
print final()

# c.
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
results('c')
print final()
# d.
results('d')
import string
def non_whitespace(strin):
	return ''.join([ l for l in strin if l not in string.whitespace])

print non_whitespace("sfvsf rg rG\n w wwfwrg \t")  # improve test case here

#e.
ml="""
line one with 20 character long
line two 

line four with 20 character long
"""
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
results('e')
print strings(ml)
#f.

import random
x = []
random.seed(1)
for _ in range(20):
 x.append(random.random())
results('f')
print(x)

#g.1
def odd_gen(n):
  for i in xrange(1,n,2):
    yield i

results('g.1')

print list(odd_gen(1000))


#g.2
results('g.2')
print ', '.join(map(str,list(xrange(1,1000,2))))
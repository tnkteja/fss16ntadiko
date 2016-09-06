#!/usr/bin/python
from __future__ import division
import random
r = random.random
rseed = random.seed

class Pretty(object):
    def __repr__(self):
        return self.__class__.__name__ + '( ' + ', '.join([str(k) + " = " + str(self.__dict__[k]) for k in sorted(self.__dict__.keys())]) +' )'

 
class Some(Pretty):
  def __init__(i, max=8): 
    i.n, i.any, i.max = 0,[],max
  def __iadd__(i,x):
    i.n += 1
    now = len(i.any)
    if now < i.max:    
      i.any += [x]
    elif r() <= now/i.n:
      i.any[ int(r() * now) ]= x 
    return i

s=Some()
print s
for i in xrange(1,999):
	s+=i
print s
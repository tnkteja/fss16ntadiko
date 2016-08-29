from __future__ import division
from collections import Counter
import random

def has_duplicates(lst):
	ctr=Counter(lst).values()
	return sum(ctr) > len(ctr)


trails=10000
count=0
for i in xrange(trails):
	count+= (1 if has_duplicates([ random.randint(1,365) for i in xrange(23) ]) else 0)

print count/trails

def gather(*args,**argv):
	print args
	print argv


gather(1,2,3,name="wvwrf",wrwr=424)

dic={1:2,2:3,3:4,5:6}
print dict(((1,2),(1,3)))



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

prob = count/trails
print "Probability %f"%(prob)
assert prob >= 0.5

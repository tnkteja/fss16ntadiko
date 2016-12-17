def func(lsts):
	return sum(map(sum,lsts))

import random

arr=[random.sample(range(0,26),random.randint(1,26)) for i in xrange(random.randint(1,26))]
for lst in arr:
	print lst, sum(lst)
print func(arr)


x={1:3}

lst=[0,x]

del lst[1]
print lst
print "gegevege wvwr.".split()
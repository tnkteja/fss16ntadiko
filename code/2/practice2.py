import random
from collections import Counter

def func(arg1,arg2):
	return list(set(arg1))[:arg2]

arg1=random.sample(range(1,20)*2,10)
print func(random.sample(arg1, 9),4)
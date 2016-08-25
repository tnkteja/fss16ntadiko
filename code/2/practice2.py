def func(arg1,arg2):
	return list(set(arg1))[:arg2]

print func(range(1,9), 4)
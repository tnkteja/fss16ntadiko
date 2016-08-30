#Classes
class newClass(object):
	"""docstring for newClass"""
	def __init__(self, arg):
		super(newClass, self).__init__()
		self.arg = arg
print newClass(None)

#Functions
def function():
	"""docstring for function"""
	return None

print function()	

#default params
def defaultParams(defaultParam1=True):
	"""docString for function"""
	return defaultParam1

print defaultParams()

#variable lists arg
def variableListsArgs(*arr):
	"""docString for function"""
	return arr

print isinstance(variableListsArgs(1,2,"3",None),tuple)

#variable dictionary args
def variableDictionaryArgs(**dic):
	"""docString for function"""
	return dic

print isinstance(variableDictionaryArgs(arg1="value1",arg2="value2"),dict)

#decorators
def decorator(f):
	"""docString for function"""
	print f.__name__,"decorated"
	return f

@decorator
def func():
	pass

#exception handling
try:
	1/0
except ZeroDivisionError as zde:
	print zde
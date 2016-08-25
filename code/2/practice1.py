#Classes
class newClass(object):
	"""docstring for newClass"""
	def __init__(self, arg):
		super(newClass, self).__init__()
		self.arg = arg

#Functions
def function():
	"""docstring for function"""
	return None

#default params
def defaultParams(defaultParam1=None):
	"""docString for function"""
	return defaultParam1

#variable lists arg
def variableListsArgs():
	pass

#decorators
def decorator():
	pass

#exception handling
try:
	1/0
except ZeroDivisionError as zde:
	print zde
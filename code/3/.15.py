

class Pretty(object):
    def __repr__(self):
        return self.__class__.__name__ + '( ' + ', '.join([str(k) + " = " + str(self.__dict__[k]) for k in sorted(self.__dict__.keys())]) +' )'

class Point(Pretty):
	"""docstring for Point"""
	def __init__(self, *arg):
		self.x,self.y = arg[:2]


	def __sub__(self,other):
		return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

x=Point(5,5)
y=Point(0,0)
print x - y
print 2
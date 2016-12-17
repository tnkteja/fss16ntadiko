from __future__ import division

class Pretty(object):
    def __repr__(self):
    	keys=self.__dict__.keys()
    	keys.sort()
        return self.__class__.__name__ + '( ' + ','.join([str(k) + " = " + str(self.__dict__[k]) for k in keys  if not k.startswith("_")]) +' )'

eucledianDistance=lambda x,y:  sum(map(lambda xi,yi: (xi-yi)**2, x, y))**0.5

print eucledianDistance((0,0,2,3,4,4),(2,2,2,4,5,2))


product=lambda *x:  reduce(mul, x) 

mean=lambda *x:  sum(x)/len(x)
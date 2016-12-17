import random,string,sys
sys.dont_write_bytecode=True

class Pretty(object):
    def __repr__(self):
        return self.__class__.__name__ + '( ' + ', '.join([str(k) + " = " + str(self.__dict__[k]) for k in sorted(self.__dict__.keys())]) +' )'


class Employee(Pretty):
    """Employee Class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self,other):
    	return self.age < other.age


print Employee(''.join(random.sample(string.ascii_lowercase,random.randint(1,26))), random.randint(1,26)) 


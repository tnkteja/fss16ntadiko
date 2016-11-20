#!/usr/bin/python
# coding: utf-8

"""
"""

__authour__="ntadiko"

from math import exp,sin,cos,pi
from operator import mul
from sys import dont_write_bytecode


from decisions import intTypeDecision, floatTypeDecision, polynomialConstraint
from dsl import problem
from objectives import functionTypeObjective
from operator import lt, add, sub


dont_write_bytecode=True

class singleObjectiveProblem(problem):

	def __init__(self,*args, **kwargs):
		super(singleObjectiveProblem, self).__init__(*args,**kwargs)

class multiObjectiveProblem(problem):

	def __init__(self):
		super(multiObjectiveProblem, self).__init__()

class schaffer(singleObjectiveProblem):

	def __init__(self,optimizer=None):
		super(schaffer, self).__init__(
			decisions=[ 
			    intTypeDecision(bounds=(-10**5,10**5))
			],
			objectives=[
			    functionTypeObjective(function=lambda x:  x**2),
			    functionTypeObjective(function=lambda x:  (x-2)**2)
			],
			optimizer=optimizer,
			type=lt
			)


class osyczka2(problem):

	def __init__(self, optimizer=None):
		super(osyczka2, self).__init__(
			decisions=[
			    intTypeDecision(name="x1",bounds=(0,10)),
			    intTypeDecision(name="x2",bounds=(0,10)),
				intTypeDecision(name="x3",bounds=(1,5)),
				intTypeDecision(name="x4",bounds=(0,6)),
				intTypeDecision(name="x5",bounds=(1,7)),
				intTypeDecision(name="x6",bounds=(0,10))
			],
			objectives=[
			    functionTypeObjective(function=lambda x1,x2,x3,x4,x5,x6:  -(25*(x1-2)**2 + (x2-2)**2 + ((x3-1)**2)*((x4-4)**2)+(x5-1)**2), type=lt),
			    functionTypeObjective(function=lambda x1,x2,x3,x4,x5,x6:  x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2, type=lt)
			],
			optimizer=optimizer,
			type=lt,
			constraints=[
			    polynomialConstraint(condition=lambda x1,x2,x3,x4,x5,x6:  x1+x2-2>=0),
			    polynomialConstraint(condition=lambda x1,x2,x3,x4,x5,x6:  6-x1-x2>=0),
			    polynomialConstraint(condition=lambda x1,x2,x3,x4,x5,x6:  2-x2+x1>=0),
			    polynomialConstraint(condition=lambda x1,x2,x3,x4,x5,x6:  2-x1+3*x2>=0),
			    polynomialConstraint(condition=lambda x1,x2,x3,x4,x5,x6:  4-(x3-3)**2-x4>=0),
			    polynomialConstraint(condition=lambda x1,x2,x3,x4,x5,x6:  (x5-3)**2+x6-4>=0)
			]
			)

class kursawe(problem):
	"""
	"""
	def __init__(self,optimizer=None):
		super(kursawe, self).__init__(
			decisions=[
			    floatTypeDecision(name="x1",bounds=(-5,5)),
			    floatTypeDecision(name="x2",bounds=(-5,5)),
				floatTypeDecision(name="x3",bounds=(-5,5))
			],
			objectives=[
				functionTypeObjective(function=lambda x1,x2,x3:  -10*(exp(-0.2*(x1**2 + x2**2)**0.5)+exp(-0.2*(x2**2 + x3**2)**0.5))),
				functionTypeObjective(function=lambda  x1,x2,x3:  sum([(abs(x)**0.8)+(5*sin(x**3)) for x in [x1,x2,x3]]))
			],
			optimizer=optimizer,
			type=lt
			)

class fonseca(problem):
	"""
	"""
	def __init__(self,n=4,optimizer=None):
		super(fonseca, self).__init__(
			decisions=[
			    intTypeDecision(name='x'+str(i+1),bounds=(-4,4)) for i in xrange(n)  
			],
			objectives=[
			   functionTypeObjective(function=lambda *x:  1-exp(-1*sum([ operator(xi,len(x)**(-0.5))**2 for xi in x])), type=lt) for operator in [sub,add]
			],
			optimizer=optimizer
			)


class _dtlz(problem):

	def __init__(self, numberOfDecisions=0, fs=[], optimizer=None):
		print "Warning about dtlz line of problem: Suggested number of decision is 4 more than numberOfObjectives"

		super(_dtlz, self).__init__(
			decisions=[
			    floatTypeDecision(name='x'+str(i+1),bounds=(0,1)) for i in xrange(numberOfDecisions)
			],
			objectives=[ 
			    functionTypeObjective(function=f, type=lt) for f in fs
			],
			optimizer=optimizer
			)
		

class dtlz1(_dtlz):
	def __init__(self, numberOfDecisions=0, numberOfObjectives=0, optimizer=None):

		k=numberOfDecisions - numberOfObjectives + 1 

		g=lambda *x:  100*( k + sum([ (x[i]-0.5)**2 - cos(20*pi*(x[i]-0.5)) for i in xrange(k,numberOfDecisions-k)]))

		fs=[lambda *x:  reduce(mul, [0.5] + list(x[:-(i+1)]) + [ ( 1- ( x[-i] if i > 0 else 0 ) ), ( 1 + g(*x) ) ]) for i in xrange(numberOfObjectives)]
		
		super(dtlz1, self).__init__(
			numberOfDecisions=numberOfDecisions,
			fs=fs,
			optimizer=optimizer,
			)

class dtlz3(_dtlz):
	def __init__(self,  numberOfDecisions=0, numberOfObjectives=0, optimizer=None):

		k=numberOfDecisions - numberOfObjectives + 1 

		g=lambda *x:  100 * (k+sum([ (x[i]-0.5)**2 - cos(20*pi*(x[i]-0.5)) for i in xrange(k,numberOfDecisions-k)]))

		fs=[lambda *x:  reduce(mul, + [ cos(xi*pi*0.5) for xi in x[:-(i+1) ] ] + [ ( sin(x[-i]*pi*0.5) if i > 0 else 1 ) , ( 1 + g(*x) ) ]) for i in xrange(numberOfObjectives)]
		
		super(dtlz1, self).__init__(
			numberOfDecisions=numberOfDecisions,
			fs=fs,
			optimizer=optimizer,
			)

class dtlz5(_dtlz):
	def __init__(self,  numberOfDecisions=0, numberOfObjectives=0, optimizer=None):

		k=numberOfDecisions - numberOfObjectives + 1

		g=lambda *x:  sum([ (x[i]-0.5)**2  for i in xrange(k,numberOfDecisions-k)])

		thetas=[ lambda *x:  (pi/(4 + g(*x)))*(1+2*g(*x)*x[i]) for i in xrange(numberOfObjectives) ]

		fs=[lambda *x:  reduce(mul, [ cos(thetai(*x)*pi*0.5) for thetai in thetas[:-(i+1) ] ] + [ ( sin(thetas[-i](*x)*pi*0.5) if i > 0 else 1 ) , ( 1 + g(*x) ) ]) for i in xrange(numberOfObjectives)]
		
		super(dtlz1, self).__init__(
			numberOfDecisions=numberOfDecisions,
			fs=fs,
			optimizer=optimizer,
			)

class dtlz7(_dtlz): 
	"""
	"""
	def __init__(self,  numberOfDecisions=0, numberOfObjectives=0, optimizer=None):

		k=numberOfDecisions - numberOfObjectives + 1

		g=lambda *x:  1+((9/k)*sum(x[k:numberOfDecisions-k]))

		fs=[ lambda *x:  x[i] for i in xrange(numberOfObjectives-1)]
		
		h=lambda *x: numberOfObjectives-sum([ (f(*x)/(1+k))*(1+sin(3*pi*f(*x))) for f in fs])  
		
		fs+=[lambda *x:  (1+g(*x))*h(*x)]
		
		super(dtlz1, self).__init__(
			numberOfDecisions=numberOfDecisions,
			fs=fs,
			optimizer=optimizer,
			)
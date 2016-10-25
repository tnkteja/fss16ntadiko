#!/usr/bin/python
# coding: utf-8
"""
"""
__authour__="ntadiko"

from math import exp,sin
from sys import dont_write_bytecode


from decisions import intTypeDecision, polynomialConstraint
from dsl import problem
from objectives import functionTypeObjective

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
			type="min")


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
			    functionTypeObjective(function=lambda x1,x2,x3,x4,x5,x6:  -(25*(x1-2)**2 + (x2-2)**2 + ((x3-1)**2)*((x4-4)**2)+(x5-1)**2)),
			    functionTypeObjective(function=lambda x1,x2,x3,x4,x5,x6:  x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2)
			],
			optimizer=optimizer,
			type="min",
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
			    intTypeDecision(name="x1",bounds=(-5,5)),
			    intTypeDecision(name="x2",bounds=(-5,5)),
				intTypeDecision(name="x3",bounds=(-5,5))
			],
			objectives=[
				functionTypeObjective(function=lambda x1,x2,x3:  -10*(exp(-0.2*(x1**2 + x2**2)**0.5)+exp(-0.2*(x2**2 + x3**2)**0.5))),
				functionTypeObjective(function=lambda  x1,x2,x3:  sum([abs(x)+5*sin(x**3) for x in [x1,x2,x3]]))
			],
			optimizer=optimizer,
			type="min"
			)

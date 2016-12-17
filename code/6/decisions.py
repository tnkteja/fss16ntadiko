#!/usr/bin/python
# coding: utf-8
"""decisions
"""
__author__ = "ntadiko"

from itertools import product
import random


from dsl import decision,constraint

class intTypeDecision(decision):
	"""IntTypeDecision
	"""
	def __init__(self,name=None,bounds=None):
		self.name=name
		self.bounds=bounds
		self.picked=set()
		
	def random(self):
		return random.randint(self.bounds[0],self.bounds[1]+1)

	def random_without_replacing(self):
		pick=None
		while True:
			pick=random.randint(self.bounds[0],self.bounds[1]+1)
			if pick not in self.picked:
				self.picked.add(pick)
				break
		return pick

	def setMutationRange(fraction):
		self.mutationRange=int(fraction*sum(map(abs,self.bounds)))

	def _isInBounds(self,x):
		return self.bounds[0] <= x <= self.bounds[1]

	def mutate(self,x):
		newX=x
		while True:
			newX=x+(random.randint(self.bounds[0],self.bounds[1]+1) * (1 if random.random() < 0.5 else -1))
			if self._isInBounds(newX):
				break
		return newX

	def __iter__(self):
		for i in xrange(self.bounds[0],self.bounds[1]):
			yield i

class enumTypeDecision(decision):
	"""enumTypeDecision
	"""
	def __init__(self):
		pass

class polynomialConstraint(constraint):
	"""
	"""
	def __init__(self,condition=None):
		self.condition=condition
		self.cache={}

	def __contains__(self,solution): # does the job but not a straight implementation
		value=self.cache.get(solution,None)
		if value == None:
			value=self.condition(*solution)
			self.cache[solution]=value
		return value




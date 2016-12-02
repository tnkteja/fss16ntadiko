#!/usr/bin/python
# coding: utf-8

"""decisions
"""
from __future__ import division

__author__ = "ntadiko"

from itertools import product
from operator import sub
import random
from sys import maxint, dont_write_bytecode


from dsl import decision,constraint

dont_write_bytecode=True

class intTypeDecision(decision):
	"""IntTypeDecision
	"""
	def __init__(self,name=None,bounds=None):
		self.name=name
		self.bounds=bounds
		self.picked=set()
		
	def random(self):
		return random.randint(self.bounds[0],self.bounds[1])

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

	def isInBounds(self,x):
		return self.bounds[0] <= x <= self.bounds[1]

	def limitToBounds(self,x):
		return max(self.bounds[0],min(x,self.bounds[1]))

	def mutate(self,x):
		newX=x
		while True:
			newX=x+(random.randint(self.bounds[0],self.bounds[1]+1) * (1 if random.random() < 0.5 else -1))
			if self.isInBounds(newX):
				break
		return newX

	def count(self, start=0,step=0,end=0, steps=1000,randomPick=True):
		step=round(step or (sub(*self.bounds[::-1])/steps)) or 1
		start= start or self.bounds[0]
		end= end or self.bounds[1]
		while start < end:
			yield (random.randint(start,start+step) if randomPick else start)
			start+=step
		if not randomPick:
			yield start

	def __iter__(self):
		for i in xrange(self.bounds[0],self.bounds[1]+1):
			yield i

class floatTypeDecision(decision):
	"""IntTypeDecision
	"""
	def __init__(self,name=None,bounds=None):
		self.name=name
		self.bounds=bounds
		self._picked=set()
		
	def random(self):
		return random.uniform(*self.bounds)

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

	def limitToBounds(self,x):
		if x < self.bounds[0]:
			return self.bounds[1]-(x-self.bounds[0])
		if x > self.bounds[1]:
			return self.bounds[0]+(x-self.bounds[1])
		return x

	def mutate(self,x):
		newX=x
		while True:
			newX=x+(self.random() * (1 if random.random() < 0.5 else -1))
			if self._isInBounds(newX):
				break
		return newX

	def count(self, start=0,step=0,end=maxint, steps=1000, randomPick=True):
		step=step or (sub(*self.bounds[::-1])/steps)
		start= max(self.bounds[0],start)
		end= min(end,self.bounds[1])
		while start < end:
			yield (random.uniform(start,start+step) if randomPick else start)
			start+=step
		if not randomPick:
			yield start

	def __iter__(self):
		start=self.bounds[0]
		step=1/1000
		while start <  self.bounds[1]:
			yield start
			start+=step


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


"""
MIT License

Copyright (c) 2016 Neela Krishna Teja Tadikonda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
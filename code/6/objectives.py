#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"

from sys import dont_write_bytecode


from dsl import objective

dont_write_bytecode=True

class functionTypeObjective(objective):

	def __init__(self, function):
		self.cache={}
		self.function=function

	def score(self,*args):
		value=self.cache.get(args,False)
		if not value:
			value=self.function(*args)
		return value

	def __call__(self,*args):
		return self.score(self,*args)

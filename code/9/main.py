#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"

from pickle import load, dump
from problems import dtlz1,dtlz3,dtlz5,dtlz7, kursawe
from operator import lt, gt
from optimizers import nsga2, gacdom, ga
from random import seed
from collections import defaultdict
from pprint import pprint
from itertools import combinations
from threading import Thread
from dsl import problem, objective
from decisions import enumTypeDecision
from utils import Pretty


class modelObjective(objective):
	def __init__(self,name,model):
		self.name=name
		self.model=model
		self.score=None
		self.type=lt

	def score(self,*solution):
		v=self.model.__cache.get(solution,0)
		if not v:
			v=self.model.run(*solution)
		return v[0]

class model(object):
	def __init__(self,problem, initialGeneration):
		self.problem=problem
		self.initialGeneration=initialGeneration
		self.objectives=[modelObjective("cdomloss",self)]
		self.__cache={}

	def __iter__(self):
		for obj in self.objectives:
			yield obj

	def run(self,*solution):
		kwargs={k:v for v in zip(["mr","cr","size","generations"],solution)}
		self.problem.setOptimizer(ga(**kwargs))
		self.problem.solve()
		self.__cache[solution]=[p.lossStatistic(p.initialGeneration,self.problem.result)]

class gatuner(problem):

	def __init__(self, problem, initialGeneration):
		super(gatuner, self).__init__(
			decisions=[
			enumTypeDecision(name="mutation", values=[0.1,0.3,0.5]),
			enumTypeDecision(name="crossover", values=["singlePoint","TwoPoint","uniform"]),
			enumTypeDecision(name="selection", values=["dominanceCount","dominanceRank","continuousDominanceLoss"]),
			enumTypeDecision(name="size",values=[50,100,150]),
			enumTypeDecision(name="generations", values=[20,40,80])
			],
			objectives=model(problem, initialGeneration)
			)

pbs=[ problem(numberOfObjectives=o,numberOfDecisions=d) for problem in [dtlz1,dtlz3,dtlz5,dtlz7] for o in [2,4,6,8] for d in [10,20,40]]

for p in pbs:
	baselinepopulations=None
	with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives)),"baselinepopulations.pickle"]),"rb") as f:
		baselinepopulations=load(f)
	pp=gatuner(p, baselinepopulations[0])
	pp.solve()
	print pp.result
	quit()

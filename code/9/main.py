#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"

from pickle import load, dump
from problems import dtlz1,dtlz3,dtlz5,dtlz7, kursawe
from operator import lt, gt
from optimizers import nsga2, gacdom, ga,de, sae
from random import seed
from collections import defaultdict
from pprint import pprint
from itertools import combinations
from threading import Thread
from dsl import problem, objective
from decisions import enumTypeDecision
from utils import Pretty


class modelObjective(objective):
	def __init__(self,name,m):
                super(modelObjective,self).__init__()
		self.name=name
		self.model=m
		self.type=lt

	def score(self,*solution):
             value=self.model.objectiveScores(*solution)[0]
             if value < self._minimumSoFar:  self._minimumSoFar=value
             elif value > self._maximumSoFar:  self._maximumSoFar=value
             return value

class model(object):
	def __init__(self,problem, initialGeneration):
		self.problem=problem
		self.initialGeneration=initialGeneration
		self.objectives=[modelObjective("cdomloss",self)]
		self.__cache={}

	def objectiveScores(self,*solution):
		v=self.__cache.get(solution,0)
		if not v:
                        kwargs={k:v for k,v in zip(["mr","cr","select","size","generations"],solution)}
			self.problem.setOptimizer(ga(**kwargs))
			self.problem.solve(initialGeneration=self.initialGeneration)
			self.__cache[solution]=v=[p.lossStatistic(p.baselineGeneration,self.problem.result)]
		return v

	def __iter__(self):
		for obj in self.objectives:
			yield obj

        def __len__(self):
            return len(self.objectives)

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
			objectives=model(problem, initialGeneration),
			optimizer=de()
			)

pbs=[ problem(numberOfObjectives=o,numberOfDecisions=d) for problem in [dtlz1,dtlz3,dtlz5,dtlz7] for o in [2,4,6,8] for d in [10,20,40]]

dic={"problem":[],
"GA Parameters (Mutation, Crossover, Select, Size, Generations)":[]
}
for p in pbs:
	baselinepopulations=None
	with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives)),"baselinepopulations.pickle"]),"rb") as f:
		baselinepopulations=load(f)
#	pp=gatuner(p, baselinepopulations[0])
#	pp.solve()
#        result=[(ind.solution,ind.objectiveScores) for ind in pp.result]
#        dic["problem"].append('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives))]))
#        with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives)),"result.pickle"]),'rb') as f:
#           result=load(f)
#           result.sort(key=lambda x:  x[1],reverse=True)
#           best=result[0]
#           dic["GA Parameters (Mutation, Crossover, Select, Size, Generations)"].append(best[0])
#        result=[(ind.solution,ind.objectiveScores) for ind in pp.result]
        dic["problem"].append('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives))]))
        with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives)),"result.pickle"]),'rb') as f:
           result=load(f)
           result.sort(key=lambda x:  x[1],reverse=True)
           best=result[0]
           with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives)),"TunedvsUntuned.txt"]),"w") as f:
			   tunedga=ga({k:v for k,v in zip(["mr","cr","select","size","generations"],best)})
			   p.setOptimizer(tunedga)
			   p.solve(repeatOn=baselinepopulations)
			   losses=map(p.lossStatistic,p.baselineGenerations,p.results)
			   print >> f,'.'.join(["tunedga",'.'.join(map(str,best[0])),p.name,str(len(p.decisions)),str(len(p.objectives))])
			   print >> f, ' '.join(map(str,losses))
			   print >> f, ''
			   p.setOptimizer(ga())
			   p.solve(repeatOn=baselinepopulations)
			   losses=map(p.lossStatistic,p.baselineGenerations,p.results)
			   print >> f,'.'.join(["ga",p.name,str(len(p.decisions)),str(len(p.objectives))])
			   print >> f, ' '.join(map(str,losses))
			   print >> f, ''

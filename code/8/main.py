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


pbs=[ problem(numberOfObjectives=o,numberOfDecisions=d) for problem in [dtlz1,dtlz3,dtlz5,dtlz7] for o in [2,4,6,8] for d in [10,20,40]]
optimizers=[nsga2, gacdom]
pms=defaultdict(list)
for p in pbs:
	baselinepopulations=[ [p.random() for _ in xrange(100)] for _ in xrange(20)]
	with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives))])+".baselinepopulations.pickle","wb") as f:
	    dump(baselinepopulations,f)
	continue
	for optimizer in optimizers:
		p.setOptimizer(optimizer)
		p.solve(repeatOn=baselinepopulations)
		pms['.'.join([optimizer.name,str(len(p.decisions)),str(len(p.objectives))])].append(map(p.lossStatitic, p.baselineGenerations,p.results))
		quit()

with open("lossStatitics.pickle","wb") as f:
	dump(dict(pms), f)
	pprint(pms)


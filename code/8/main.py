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

pbs=[ problem(numberOfObjectives=o,numberOfDecisions=d) for problem in [dtlz1,dtlz3,dtlz5,dtlz7] for o in [2,4,6,8] for d in [10,20,40]]
optimizers=[nsga2,gacdom]
pms=defaultdict(list)

def target(p,pms,optimizers):
	baselinepopulations=None
	with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives))])+".baselinepopulations.pickle","rb") as f:
	    baselinepopulations=load(f)
	with open('.'.join([p.name,str(len(p.decisions)),str(len(p.objectives)),"out"]),'w') as f:
		print >> f, "Started ..."
		f.flush()
		for optimizer in optimizers:
			p.setOptimizer(optimizer=optimizer())
			p.solve(repeatOn=baselinepopulations)
			pms['.'.join([p.name,str(len(p.decisions)),str(len(p.objectives)),optimizer.__name__])].append(map(p.lossStatitic, p.baselineGenerations,p.results))
		print >> f, "Done .."

threads=[Thread(target=target, args=[p,pms, optimizers]) for p in pbs]
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()
with open("nsga2lossStatistic.pickle","wb") as f:
	pms=dict(pms)
	dump(pms, f)
	pprint(pms)

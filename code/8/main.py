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


problem=kursawe
p=problem(optimizer=gacdom())
p.solve()
p.plotParetoFrontier(p.result).show()
quit()
# pbs=[dtlz1,dtlz3,dtlz5,dtlz7]
# baselinepopulations=[ [p.random() for _ in xrange(100)] for _ in xrange(20)]
# with open("baselinepopulations.pickle","wb") as f:
#     dump(baselinepopulations,f)
# pms=defaultdict(list)
# for optimizer in [sae(),mwse()]:
# 	p.setOptimizer(optimizer)
# 	p.solve(repeatOn=baselinepopulations)
# 	pms[optimizer.name].append(map(p.lossStatitic, p.baselineGenerations,p.results))

# with open("lossStatitics.pickle","wb") as f:
# 	dump(pms, f)
# 	pprint(pms)


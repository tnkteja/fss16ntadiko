#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"

from pickle import load, dump
from problems import schaffer,osyczka2,kursawe,dtlz1,fonseca,dtlz7
from operator import lt, gt
from optimizers import sa,sae,mwse,de, mws, ga, nsga2
from random import seed
from collections import defaultdict
from pprint import pprint

problem=dtlz7
p=problem()
baselinepopulations=[ [p.random() for _ in xrange(100)] for _ in xrange(20)]
with open("baselinepopulations.pickle","wb") as f:
    dump(baselinepopulations,f)
pms=defaultdict(list)
for optimizer in [sae(),de(),mwse()]:
	p.setOptimizer(optimizer)
	p.solve(repeatOn=baselinepopulations)
	pms[optimizer.name].append(map(p.lossStatistic, p.baselineGenerations,p.results))

with open("lossStatisics.pickle","wb") as f:
        pms=dict(pms)
	dump(pms, f)
	pprint(pms)


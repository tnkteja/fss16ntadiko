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
p=problem(optimizer=de())
baselinepopulations=None
with open("baselinepopulations.pickle","rb") as f:
    baselinepopulations=load(f)
pms={"de":[]}
p.solve(repeatOn=baselinepopulations)
pms["de"].append(map(p.lossStatitic, p.baselineGenerations,p.results))

with open("lossStatitics_de.pickle","wb") as f:
	dump(pms, f)
	pprint(pms)


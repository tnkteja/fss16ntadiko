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


problem=kursawe
p=problem(optimizer=ga())
baselinepopulations=[ [p.random() for _ in xrange(100)] for _ in xrange(20)]
p.solve(repeatOn=baselinepopulations)
with open("_".join([p.name,p.optimizer.name])+".pickle","wb") as f:
	dump(p.results,f)



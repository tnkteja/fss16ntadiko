#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"


from problems import schaffer,osyczka2,kursawe,dtlz1,fonseca
from operator import lt, gt
from optimizers import sa,sae,mwse,de, mws, ga, nsga2
from random import seed
from matplotlib import pyplot as plt

problem=kursawe
p=problem(optimizer=ga())
p.solve()
p.plotParetoFrontier(p.result).show()
quit()
baselinepopulations=[ [p.random() for _ in xrange(4)] for _ in xrange(2)]
p.solve(repeatOn=baselinepopulations)
print p.result
p.makeReferenceSetScores(p.result,limitTo=4)
print p.referenceSet
print p.interGenerationalDistance(map(lambda x:  x[1],p.results[1]),map(lambda x:  x[1] ,p.referenceSet))
print p.interGenerationalDistance(map(lambda x:  x[1],p.results[1]),map(lambda x:  x[1] ,p.referenceSet))

#dtlz1(numberOfDecisions=10, numberOfObjectives=2, optimizer=sa()).solve()
#dtlz1(numberOfDecisions=10, numberOfObjectives=2, optimizer=mws()).solve()
#pareto=dtlz1(numberOfDecisions=10, numberOfObjectives=2, optimizer=de()).solve()

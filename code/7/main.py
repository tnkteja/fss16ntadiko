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

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#baselinepopulations=[ [p.random() for _ in xrange(100)] for _ in xrange(20)]
problem=kursawe
p=problem(optimizer=mwse())
p.solve()

p.plotParetoFrontier(p.result).show()

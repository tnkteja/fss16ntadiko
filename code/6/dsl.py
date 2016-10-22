#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"

from itertools import product
from sys import dont_write_bytecode


from utils import Pretty

dont_write_bytecode=True

class problem(Pretty):
    """
    """

    def __init__(self,decisions=None,objectives=None,optimizer=None,type=None):
        self.decisions,self.objectives,self.optimizer,self.type=decisions,objectives,optimizer,type

    def random(self,withReplacement=False):
        """random"""
        return tuple([ decision.random() for decision in self.decisions])

    def randomSample(self,k,withReplacement=False):
        sols= [] if withReplacement else set()
        add=getattr(sols,"append" if withReplacement else "add")
        while(len(sols)<k):
                add(tuple([ decision.random() for decision in self.decisions]))
        return sols

    def objectiveScores(self,solution):
        return tuple([ objective.score(*solution) for objective in self.objectives])

    def solve(self):
        self.optimizer.setProblem(self)
        self.optimizer.run()

class optimizer(Pretty):
    """
    """

    def __init__(self):
        self.problem=None

    def setProblem(self,problem):
        self.problem=problem

class decision(Pretty):

    def __init__(self):
        pass

class objective(Pretty):

    def __init__(self):
        pass
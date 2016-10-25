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

    def __init__(self,decisions=None,objectives=None,optimizer=None,type=None,constraints=[]):
        self.decisions,self.objectives,self.optimizer,self.type,self.constraints=decisions,objectives,optimizer,type,constraints

    def random(self,withReplacement=False):
        """random"""
        while True:
            newSolution=tuple([ decision.random() for decision in self.decisions])
            if self.checkConstraints(newSolution):
                return newSolution


    def checkConstraints(self,solution):
        for constraint in self.constraints:
            if solution not in constraint:
                return False
        return True


    def randomSample(self,k,withReplacement=False):
        sols= [] if withReplacement else set()
        add=getattr(sols,"append" if withReplacement else "add")
        while(len(sols)<k):
            newSolution = tuple([ decision.random() for decision in self.decisions])
            if self.checkConstraints(newSolution):
                add(newSolution)
        return sols

    def objectiveScores(self,solution):
        x=tuple([ objective.score(*solution) for objective in self.objectives])
        print x
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

class constraint(Pretty):

    def __init__(self):
        pass

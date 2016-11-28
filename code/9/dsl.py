#!/usr/bin/python
# coding: utf-8
"""
"""

from __future__ import division

__author__ = "ntadiko"

from bisect import insort
from collections import Counter
from itertools import product
import logging
from math import e
from operator import lt, gt, add
from sys import dont_write_bytecode

try:
    from matplotlib import pyplot as plt
except ImportError:
    plt=object()


from borrowed.borrowed import HyperVolume, a12
from utils import Pretty, eucledianDistance
from stats import median, mean

dont_write_bytecode=True

class problem(Pretty):
    """
    """

    def __init__(self,decisions=None,objectives=None,optimizer=None,type=gt,constraints=[],optimizers=[]):
        self.name=self.__class__.__name__
        self.decisions,self.objectives,self.optimizer,self.type,self.constraints=decisions,objectives,optimizer,type,constraints
        self.minimumInfamousSum=self.maximumInfamousSum=0
        self.minimumInfamousSum=self.maximumInfamousSum=self.infamousSum(self.objectiveScores(self.random()))
        self.__computationCache={}

    def setOptimizer(self, optimizer):
        self.optimizer=optimizer

    def random(self,withReplacement=False):
        """random"""
        while True:
            newSolution=tuple([ decision.random() for decision in self.decisions])
            if self.checkConstraints(newSolution):
                return newSolution

    def mutate(self,solution):
        return tuple([decision.mutate(solution[i]) for i,decision in enumerate(self.decisions)])

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
        return list(sols)

    def objectiveScores(self,solution):
        scores=tuple([ objective.score(*solution) for objective in self.objectives])
        return scores


    def binaryDomination(self,one,other):
        """
        All should be better or equal, with atleast one better.
        """
        atleastOneBetter=False
        for i,objective in enumerate(self.objectives):
            better,worse= (lt,gt) if objective.type is lt else (gt,lt)
            if better(one[i],other[i]):
                atleastOneBetter=True
            elif worse(one[i],other[i]):
                return False
        return atleastOneBetter

    def continuousDomination(self,one, other):
        lossOneFromOther=lossOtherFromOne=0
        for i,objective in enumerate(self.objectives):
            oneNormalised=objective.normalise(one[i])
            otherNormalised=objective.normalise(other[i])
            #Exponential magnification of difference
            lossOneFromOther+=-1*e**((-1 if objective.type is lt else 1)*(oneNormalised-otherNormalised)/len(self.objectives))
            lossOtherFromOne+=-1*e**((-1 if objective.type is lt else 1)*(otherNormalised-oneNormalised)/len(self.objectives))
        return lossOneFromOther < lossOtherFromOne

    def continuousDominance(self,one, generation):
        loss=0
        for i,other in enumerate(generation):
            if one is other:
                continue
            for j, objective in enumerate(self.objectives):
                oneNormalised=objective.normalise(one.objectiveScores[j])
                otherNormalised=objective.normalise(other.objectiveScores[j])
                loss+=-1*e**((-1 if objective.type is lt else 1)*(oneNormalised-otherNormalised)/len(self.objectives))
        one.fitness=-loss
        return loss

    def dominanceRank(self,individual, generation, dominates=None):
        rank=0
        for i,other in enumerate(generation):
            rank=rank + (0 if individual.dominates(other) else 1)
        individual.fitness=-rank
        return rank

    def dominanceCount(self,individual,generation):
        count=0
        for i,otherindividual in enumerate(generation):
            count=count + (1 if individual.dominates(otherindividual) else 0)
        individual.fitness=count
        return count

    def dominanceDepth(self):
        pass

    def infamousSum(self,objectivesScores):
        s=0
        for i,objective in enumerate(self.objectives):

                s+= (-1 if objective.type == lt else 1)* objectivesScores[i]

        if s < self.minimumInfamousSum:  self.minimumInfamousSum=s
        elif s > self.maximumInfamousSum:  self.maximumInfamousSum=s

        return s

    def normalisedScore(self,sol):
        return (self.infamousSum(self.objectiveScores(sol))-self.preRunMinimumInfamousSum)/(self.preRunMaximumInfamousSum-self.preRunMinimumInfamousSum)

    def preRun(self,samples=1000):
        logging.info(self.__class__.__name__,"-> preRun")
        scores=[]
        for sample in self.randomSample(1000, withReplacement=True):
            scores.append(self.objectiveScores(sample))
            self.infamousSum(self.objectiveScores(sample))

        self.preRunMinimumInfamousSum=self.minimumInfamousSum
        self.preRunMaximumInfamousSum=self.maximumInfamousSum
        # Set the prerun results
        for i,objective in enumerate(self.objectives):
            objective.initialisePreRunMinMax()

    def solve(self, initialGeneration=[],repeatOn=[]):
        self.preRun()
        self.optimizer.setProblem(self)
        self.results=[]
        self.baselineGenerations=[]
        if not repeatOn:
            self.optimizer.run(initialGeneration=initialGeneration)
            self.result=self.optimizer.results
            self.baselineGeneration=self.optimizer.baselineGeneration
            return
        for initialPopulation in repeatOn:
            self.optimizer.run(initialGeneration=initialPopulation)
            self.baselineGenerations.append(self.optimizer.baselineGeneration)
            self.results.append(self.optimizer.results)

    def plotParetoFrontier(self,paretoFrontier):
        plt.figure(0)
        print(zip(*map(lambda ind:  ind.objectiveScores,paretoFrontier)))
        plt.plot(*(zip(*map(lambda ind:  ind.objectiveScores,paretoFrontier))+["bs"]))
        return plt

    def makeReferenceSetScores(self,paretoFrontiers, limitTo=10):
        extendedParetoFrontier=reduce(add,paretoFrontiers)
        referenceSet=[]
        for pareto in extendedParetoFrontier:
            insort(referenceSet,(len(extendedParetoFrontier)-self.dominanceCount(pareto,extendedParetoFrontier),pareto))

        self.referenceSet=[ referenceSet[i][1] for i in xrange(limitTo)]
        return self.referenceSet

    def _closestVector(self,x,Y):
        """Closest eucledian point from  point x.
        """
        return min([ ( sum(map(lambda xi,yi:  (yi-xi)**2, y, x))**0.5, y ) for y in Y ], key=lambda x: x[0])

    """
    Type 2 Comparision operator
    """
    def krallbstopmethod(self,lives,lastGeneration,currentGeneration):
        noImprovementOnAnything=True
        for i,objective in enumerate(self.objectives):
            boolean=a12(map(lambda ind:  ind.objectiveScores[i],lastGeneration),map(lambda ind:  ind.objectiveScores[i],currentGeneration))
            if (objective.type is lt and not boolean) or (objective.type is gt and boolean):
                noImprovementOnAnything=False
                lives+=5
        if noImprovementOnAnything:
            lives-=1
        return lives

    """
    Type 3 Comparision Operators
    """
    def spread(self,paretoFrontierScores,referenceSetScores):
        """Spread is also known as diversity. It is calculated for a set of objectiveScores.
        """
        # Sort the paretoFrontierScores based on the weight of each participating objective.
        objectiveScores=(0.02095599670188364, 0.6778384360925239, 0.7857142857142857, 0.0)
        weights=map(lambda i:  10**(len(objectiveScores)-i-1), xrange(len(objectiveScores)))
        sortingkey=lambda objectiveScores:  sum(map(lambda os,w:  os*w, objectiveScores, weights))
        sortedParetoFrontierScores = sorted(paretoFrontierScores,key=sortingkey)
        sortedReferenceSetScores = sorted(referenceSetScores,key=sortingkey)
        distanceFromFirstReferenceObjectiveScores=self._closestVector(sortedReferenceSetScores[0], sortedParetoFrontierScores)[0]
        distanceFromLastRefenceObjectiveScores=self._closestVector(sortedReferenceSetScores[-1], sortedParetoFrontierScores)[0]
        gaps=[ eucledianDistance(sortedParetoFrontierScores[i], sortedParetoFrontierScores[i+1]) for i in xrange(len(sortedParetoFrontierScores)-1)]
        averageGap=sum(gaps)/len(gaps)
        gapAbsoluteDeviationSum = sum([ abs(gap-averageGap) for gap in gaps])
        return (distanceFromFirstReferenceObjectiveScores + distanceFromLastRefenceObjectiveScores + gapAbsoluteDeviationSum) / (distanceFromFirstReferenceObjectiveScores + distanceFromLastRefenceObjectiveScores + (len(sortedParetoFrontierScores)-1)*averageGap )

    def interGenerationalDistance(self, paretoFrontierScores, referenceSetScores):
        """Inter generational distance - it is a measure of how good are you to the best known ?
        """
        return sum([ self._closestVector(other,paretoFrontierScores)[0]  for other in referenceSetScores])/len(referenceSetScores)

    def hypervolume(self,paretoFrontier, referencePoint=None):
        """
        """
        referencePoint= referencePoint or [ (objective._maximumSoFar if objective.type == lt else objective._minimumSoFar) for objective in self.objectives]
        return HyperVolume(referencePoint).compute(paretoFrontier)

    def lossStatistic(self, baselineGeneration, paretoFrontier):
        return sum([ self.continuousDominance(refInd, paretoFrontier) for refInd in baselineGeneration ])

class optimizer(Pretty):
    """
    """

    def __init__(self):
        self.problem=None
        self.name=self.__class__.__name__
        self.baselineGeneration=None


    def setProblem(self, problem):
        self.problem=problem
        self.domination=self.problem.continuousDomination
        self.fitness=self.problem.dominanceCount

    def preRun(self,samples=1000):
        logging.info(self.__class__.__name__,"-> preRun")
        scores=[]
        for sample in self.problem.randomSample(1000):
            scores.append(self.problem.objectiveScores(sample))



class decision(Pretty):

    def __init__(self):
        pass

class objective(Pretty):

    def __init__(self):
        self._minimumSoFar=self._maximumSoFar=0

    def initialisePreRunMinMax(self):
        self.preRunMinimum,self.preRunMaximum=self._minimumSoFar,self._maximumSoFar

    def normalise(self,x):
        mi=self.bounds[0] or self.preRunMinimum
        ma=self.bounds[1] or self.preRunMaximum
        return (x-mi)/(ma-mi)

class constraint(Pretty):

    def __init__(self):
        pass

class individual(Pretty):

    def __init__(self,problem,optimizer,solution,objectiveScores):
        self.solution=solution
        self.objectiveScores=objectiveScores
        self.fitness=None
        self.__dominancedepth=None
        self.__dominanceCount=None
        self.__dominanceRank=None
        self.__problem=problem
        self.__optimizer=optimizer

    def __lt__(self,other):
        return self.fitness < other.fitness

    def __eq__(self,other):
        return self.fitness == other.fitness

    def dominates(self,other):
        return self.__optimizer.domination(self.objectiveScores,other.objectiveScores)

    def measureFitness(self,generation):
        self.fitness=self.__optimizer.fitness(self,generation)

    def __rshift__(self,other):
        return self.__optimizer.domination(self.objectiveScores,other.objectiveScores)

class experiment(Pretty):
    def __init__(self):
        pass

class population(Pretty):
    def __init__(self,population=[]):
        self.population=population
        self.sortedpopulation=sorted(self.population)
        self.mean = sum(self.sortedpopulation)/len(self.population)
        self.median = median(self.sortedpopulation, isSorted=True)
        self.mode = max(Counter(self.population).items(),key=lambda x: x[1])
        self.averageDeviation = sum(map(lambda x:  abs(x-self.mean),self.population))/len(self.population)
        self.variance = sum(map(lambda x:  (x-self.mean)**2,self.population))/len(self.population)
        self.standardDeviaton=(self.variance)**0.5

    def mean():
        return self.sum/len(self.sortedpopulation)


    def append(self, m):
        insort(self.sortedpopulation, m)

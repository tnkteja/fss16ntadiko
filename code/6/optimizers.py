#!/usr/bin/python
# coding: utf-8
"""
"""

from __future__ import print_function, division

__author__="ntadiko"

from sys import dont_write_bytecode
from itertools import product
from math import exp
import random


from dsl import optimizer

dont_write_bytecode=True

class sa(optimizer):
    """Simulated Annealing
       Also add code to catch last nbest iterations in the list.
    """
    def __init__(self, **kwargs):
        self.cache={}

    def neighbour(self,x):  
        return tuple([decision.mutate(x[i]) for i,decision in enumerate(self.problem.decisions)])

    def objectivesSum(self,sol):
        value=self.cache.get(sol,False)
        if not value:
            value=sum(self.problem.objectiveScores(sol))
        return value

    def energy(self,sol):
        return (self.objectivesSum(sol)-self.min)/(self.max-self.min)

    def better(self,x,y):
        if self.problem.type=="min":
            return x < y
        return x > y

    def run(self,K=1000):
        samples=self.problem.randomSample(1000)
        objectivesSum=[ self.objectivesSum(sample) for sample in samples]
        self.min=min(objectivesSum)
        self.max=max(objectivesSum)
        emax=-1
        bestSolution=currentSolution=self.problem.random()
        bestEnergy=currentEnergy=self.energy(currentSolution)
        for k in xrange(K,0,-1):
            if not self.better(currentEnergy,emax):
                if k%25 ==0:
                    print(", %.4d "%(1000-k),end='')
                newSolution=self.neighbour(currentSolution) # I am choosing a neighbour to jump
                newEnergy=self.energy(newSolution) # This neighbour gives me some energy
                #If the new energy I found is better than what I found so far, let me update
                # my best solution variables and keep them with me.
                if self.better(newEnergy,bestEnergy):
                    bestEnergy,bestSolution=newEnergy,newSolution
                    print('!',end='')
                #If the new energy I found is less than the last energy I found, I need to do better
                if not self.better(newEnergy,currentEnergy):
                    currentEnergy,currentSolution=newEnergy,newSolution
                    print('+',end='')
                #If I didn't a better move and my temp is high, high prob jumping from your new solution
                elif exp(-(currentEnergy-newEnergy)/(k/K)) > random.random():
                    currentSolution=newSolution
                    print('?',end='')
                print('.',end='')
                k-=1
                print('\n' if k%25 ==0 else '',end='')
        print()
        print('bestEnergy: ',bestEnergy,"bestSolution: ",bestSolution,"bestScore",str(self.objectivesSum(bestSolution)))

        print()
        print('-'*36,end='')
        print()
        print("© 2016 MIT, Neela Krishna Teja Tadikonda")


class mws(optimizer):
    """MaxWalkSat
    """
    def __init__(self):
        self.cache={}
        self.maxtries=20

    def score(self,sol):
        return sum(self.problem.objectiveScores(sol))

    def varyOn(self,pivot=None,decision=None):
        i,decision=decision
        # for j in xrange(decision.bounds[0],decision.bounds[1]+1):
        #     pivot[i]=j
        #     yield pivot
        for j in xrange(0,10):
              pivot[i]=decision.bounds[0] + int(j/10*(decision.bounds[1] - decision.bounds[0]))
              yield pivot

    def run(self, maxtries=20, maxchanges=50, p=0.5):
        maxtries=maxtries or self.maxtries
        maxchanges=maxchanges or self.maxchanges
        solb=None
        out=''
        for i in xrange(maxtries):
            out+="Retry %.2d"%(i)+' : '
            sol = self.problem.random()
            for j in xrange(maxchanges):
                sol = solb or sol
                sol=list(sol)
                if self.score(sol) < -2000:
                    return sol
                randomsetting=random.choice(self.problem.decisions)
                i=self.problem.decisions.index(randomsetting)
                # At some probability jump around
                if p < random.random():
                    randomsettingvalue=sol[self.problem.decisions.index(randomsetting)]
                    sol[i]=randomsetting.mutate(randomsettingvalue)
                    out+='?'
                # Then, at probability (1-p), fixate on one variable and try all its 
                # values in (say) increments of (max-min)/10 (and use the value that most 
                # improves the score function).
                else:
                    better= (min if self.problem.type == "min" else max)
                    solb=better(self.varyOn(pivot=sol,decision=(i,randomsetting)),key=lambda x:  self.score(x))
                    out+='!'
            out+='\n'
        out+="\n Solution : "+ ','.join(map(str,solb))+", Score : "+str(self.score(solb))
        out+="\n\n Copyright 2016, Neela Krishna Teja Tadikonda"
        print(out)
        print

class ga(optimizer):
    """Genetic Algorithm
    """
    def __init__(self):
        pass

class de(optimizer):
    """Diffrential Evolution
    """
    def __init__(self):
        pass
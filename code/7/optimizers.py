#!/usr/bin/python
# coding: utf-8

"""
"""

from __future__ import print_function, division

__author__="ntadiko"

from bisect import insort, bisect_left, bisect_right
from collections import defaultdict, Counter
from sys import dont_write_bytecode, maxint
from itertools import product, izip
import logging
from math import exp
from operator import lt,gt
import random


from dsl import optimizer, individual

dont_write_bytecode=True

class sa(optimizer):
    """Simulated Annealing
       Also add code to catch last nbest iterations in the list.
    """
    def __init__(self, *args, **kwargs):
        super(sa,self).__init__()
        self.cache={}

    def energy(self,sol):
        return (self.problem.infamousSum(self.problem.objectiveScores(sol))-self.problem.preRunMinimumInfamousSum)/(self.problem.preRunMaximumInfamousSum-self.problem.preRunMinimumInfamousSum)

    def run(self,K=10000, era=100,initialSolution=None):
        emax=3
        bestSolution=currentSolution=initialSolution or self.problem.random()
        bestEnergy=currentEnergy=self.energy(currentSolution)
        lives=6
        eventsCounter=Counter()
        frontier=[]
        for k in xrange(K,0,-1):
            #if currentEnergy < emax:
            if lives > 0:
                if k%era == 0:
                    print('\n',end='')
                    lives = 5 if eventsCounter['!'] > 0 else lives-1
                    eventsCounter['!']=0
                    print(", %.4d "%(K-k),end='')

                newSolution=self.problem.mutate(currentSolution) # I am choosing a neighbour to jump
                newEnergy=self.energy(newSolution) # This neighbour gives me some energy

                #If the new energy I found is better than what I found so far, let me update
                # my best solution variables and keep them with me.
                if newEnergy > bestEnergy:
                    bestEnergy,bestSolution=newEnergy,newSolution
                    eventsCounter['!']+=1
                    frontier=[individual(self.problem,self,bestSolution,self.problem.objectiveScores(bestSolution))]
                    print('!',end='')

                #If the new energy I found is less than the last energy I found, I need to do better
                elif newEnergy < currentEnergy:
                    currentEnergy,currentSolution=newEnergy,newSolution
                    eventsCounter['+']+=1
                    print('+',end='')
                #If I didn't a better move and my temp is high, high prob jumping from your new solution
                else:
                    frontier.append(individual(self.problem,self,newSolution,self.problem.objectiveScores(newSolution)))
                    if exp((currentEnergy-newEnergy)/(k/K)) > random.random()*2:
                        currentSolution=newSolution
                        eventsCounter['?']+=1
                        print('?',end='')
                print('.',end='')
                k-=1
                
        print()
        print('bestEnergy: ',bestEnergy,"bestSolution: ",bestSolution,"bestScore",str(self.problem.infamousSum(self.problem.objectiveScores(bestSolution))))

        print()
        print('-'*36,end='')
        print()
        print("© 2016 MIT, Neela Krishna Teja Tadikonda")
        self.result=individual(self.problem, self,bestSolution,self.problem.objectiveScores(bestSolution))
        self.frontier=frontier

class sae(sa):
    def __init__(self):
        super(sae, self).__init__()

    def run(self,initialGeneration=None):
        initialGeneration = initialGeneration or self.problem.randomSample(100)
        self.results=[]
        for solution in initialGeneration:
            lives=1
            while lives > 0:
                lives-=1
                super(sae, self).run(initialSolution=solution)
                self.results.append(self.result)


class mws(optimizer):
    """MaxWalkSat
    """
    def __init__(self):
        super(mws,self).__init__()
        self.cache={}
        self.maxtries=20

    def score(self,sol):
        return (self.problem.infamousSum(self.problem.objectiveScores(sol))-self.problem.preRunMinimumInfamousSum)/(self.problem.preRunMaximumInfamousSum-self.problem.preRunMinimumInfamousSum)

    def varyOn(self,pivot=None,decision=None):
        i,decision=decision
        for v in decision.count(steps=1000,randomPick=True):
              pivot[i]=v
              yield tuple(pivot)

    def run(self, initialSolution=None,maxtries=20, maxchanges=100, p=0.5):
        maxtries=maxtries or self.maxtries
        maxchanges=maxchanges or self.maxchanges
        solb=sol=initialSolution or self.problem.random()
        out=''
        lives=5
        eventsCounter=Counter()
        frontier=[]
        for i in xrange(maxtries):
            if lives <0:
                break
            lives = 5 if eventsCounter['!'] > 0 else lives-1
            eventsCounter['!']=0
            print("Retry %.2d / %d"%(i,i+lives)+' : ',end='')
            for j in xrange(maxchanges):
                sol=list(sol)
                # if self.score(sol) > 5:
                #     self.result=solb,self.problem.objectiveScores(solb)
                #     print(out)
                #     return
                randomsetting=random.choice(self.problem.decisions)
                i=self.problem.decisions.index(randomsetting)
                # At some probability jump around
                if p > random.random():
                    randomsettingvalue=sol[self.problem.decisions.index(randomsetting)]
                    sol[i]=randomsetting.mutate(randomsettingvalue)
                # Then, at probability (1-p), fixate on one variable and try all its 
                # values in (say) increments of (max-min)/10 (and use the value that most 
                # improves the score function).
                else:
                    sol=max(self.varyOn(pivot=sol,decision=(i,randomsetting)),key=lambda x:  self.score(x))
                if self.score(sol) > self.score(solb):
                    solb=sol
                    frontier=[individual(self.problem,self,solb,self.problem.objectiveScores(solb))]
                    eventsCounter['!']+=1
                    print('!',end='')
                else:
                    frontier.append(individual(self.problem,self,sol,self.problem.objectiveScores(sol)))
                    print('.',end='')
            sol=self.problem.random()
            print('\n',end='')
        print("\n Solution : "+ ','.join(map(str,solb))+", Score : "+str(self.problem.infamousSum(self.problem.objectiveScores(solb))),end='')
        print("\n\n Copyright 2016, Neela Krishna Teja Tadikonda")
        self.result=individual(self.problem,self,solb,self.problem.objectiveScores(solb))
        self.frontier=frontier

class mwse(mws):
    def __init__(self):
        super(mwse, self).__init__()

    def run(self,initialGeneration=None):
        initialGeneration = initialGeneration or self.problem.randomSample(100)
        self.baselineGeneration=[ individual(self.problem,self,solution, self.problem.objectiveScores(solution)) for solution in initialGeneration]
        self.results=[]
        for solution in initialGeneration:
            super(mwse, self).run(initialSolution=solution)
            self.results.append(self.result)

class ga(optimizer):
    """Genetic Algorithm
    """
    def __init__(self):
        super(ga,self).__init__()
        self.crossover=self.singlePointCrossover

    def singlePointCrossover(self,one,other,r=0.3):
        singlePoint=len(self.problem.decisions)//2
        newSolution=one.solution[:singlePoint]+other.solution[singlePoint:]
        newindividual=individual(self.problem,self, newSolution, None)
        return newindividual

    def mutate(self,individual, rate=0.1):
        individual.solution = list(individual.solution)
        for i,decision in enumerate(self.problem.decisions):
            if random.random() < 0.2:
                individual.solution[i]=decision.random()
        individual.solution=tuple(individual.solution)
        individual.objectiveScores=self.problem.objectiveScores(individual.solution)
        return individual
        

    def elitism(self, currentGeneration,retainSize):
        sortedCurrentGeneration=[]
        for individual in currentGeneration:
            self.fitness(individual, currentGeneration)
            insort(sortedCurrentGeneration, individual)
        return sortedCurrentGeneration[-retainSize:]

    def setProblem(self,problem):
        super(ga, self).setProblem(problem)
        self.domination=self.problem.binaryDomination
        self.fitness=self.problem.dominanceCount

    def run(self, size=100,generations=100):
        currentGeneration=[ individual(self.problem,self,solution, self.problem.objectiveScores(solution)) for solution in self.problem.randomSample(size)]
        g=0
        lives=1
        for g in xrange(generations):
            if lives < 0:
                break
            lives-=1
            offspring=[]
            offspring.extend([ self.mutate(self.crossover(*random.sample(currentGeneration,2))) for _ in xrange(size)])
            lastGeneration=currentGeneration
            currentGeneration.extend(offspring)
            currentGeneration=self.elitism(currentGeneration, size)
            lives=self.problem.krallbstopmethod(lives,lastGeneration,currentGeneration)
            print("Generation ",g+1,'/',g+lives, currentGeneration)
            g+=1
        paretoFrontier=currentGeneration
        print('\n Pareto Frontier -',paretoFrontier)
        self.results=paretoFrontier


class nsga2(ga):
    """
    Non dominated Sorting, NSGA2 algorithm.
    """
    def __init__(self):
        super(nsga2, self).__init__()

    def setProblem(self, problem):
        super(nsga2, self).setProblem(problem)
        self.domination=self.problem.binaryDomination
        self.fitness=self.problem.dominanceCount

    def fastNonDominatedSort(self,currentGeneration):
        """First Ranking Method
        """
        underdogs=defaultdict(list)
        overdogscount=defaultdict(int)
        frontiers=[[]]
        sortedGeneration=[]
        for i,ind in enumerate(currentGeneration):
            for j in xrange(i+1,len(currentGeneration)-1):
                if ind.dominates(currentGeneration[j]):
                    underdogs[ind].append(currentGeneration[j])
                    overdogscount[currentGeneration[j]]+=1
                elif currentGeneration[j].dominates(ind):
                    underdogs[currentGeneration[j]].append(ind)
                    overdogscount[ind]+=1
            if overdogscount[ind] is 0:
                ind.fitness=0
                frontiers[0].append(ind)
        i=0
        while frontiers[i]:
            nextFrontier=[]
            for j,indfron in enumerate(frontiers[i]):
                for k,indunder in enumerate(underdogs[indfron]):
                    overdogscount[indunder]-=1
                    if overdogscount[indunder] is 0:
                        indunder.fitness=i+1
                        nextFrontier.append(indunder)
            frontiers.append(nextFrontier)
            i+=1
        frontiers.pop()

        return frontiers

    def cuboidSorting(self,frontier, limitTo):
        if len(frontier) <3:
            return frontier[:limitTo]
        Ip={ ind:0 for ind in frontier}
        for i,objective in enumerate(self.problem.objectives):
            frontier.sort(key=lambda ind:  ind.objectiveScores[i])
            gaps=[(frontier[1].objectiveScores[i]-frontier[0].objectiveScores[i], frontier[0]),(frontier[-1].objectiveScores[i]-frontier[-2].objectiveScores[i], frontier[-1])]
            for j in xrange(1,len(frontier)-2):
                insort(gaps, (frontier[j+1].objectiveScores[i]-frontier[j-1].objectiveScores[i] ,frontier[j]))
            for gap,ind in gaps:
                Ip[ind]+=(gap-gaps[0][0])/(gaps[-1][0]-gaps[0][0]+(1/maxint))
        frontier.sort(key=lambda ind:  Ip[ind],reverse=True)
        return frontier[:limitTo]

    def elitism(self, currentGeneration,retainSize):
        frontiers=self.fastNonDominatedSort(currentGeneration)
        selection=[]
        for i,frontier in enumerate(frontiers):
            if len(selection) + len(frontier) > retainSize:
                break
            selection.extend(frontier)
        remaining=retainSize-len(selection)
        selection.extend(self.cuboidSorting(frontiers[i],remaining))
        return selection


class de(optimizer):
    """Diffrential Evolution
    """
    def __init__(self):
        super(de,self).__init__()

    def selection(self,*args):
        return enumerate(*args)

    def extrapolationParticipantPairs(self,solution, generation):
        participants=None
        while True:
            participants=random.sample(generation,3)
            if all([solution != ind.solution for ind in participants]):
                break
        return participants

    def extrapolate(self,ind,participants,cf,f):
        X,Y,Z=participants
        new=list(ind.solution)
        noneChanged=True
        while noneChanged:
            for i,decision in enumerate(ind.solution):
                if random.random() < cf:
                    noneChanged=False
                    new[i]=self.problem.decisions[i].limitToBounds(X.solution[i]+f*(Y.solution[i]-Z.solution[i]))
        return individual(self.problem, self, tuple(new), self.problem.objectiveScores(new))

    def setProblem(self,problem):
        super(de, self).setProblem(problem)
        self.domination=self.problem.continuousDomination
        self.fitness=self.problem.dominanceCount

    def run(self,initialGeneration=[],generations=100, np=10, f=0.75, cf=0.3, epsilon=0.01):
        self.np = 10 * len(self.problem.decisions)
        paretoFrontier=nextGeneration=currentGeneration= [ individual(self.problem,self,solution, self.problem.objectiveScores(solution)) for solution in initialGeneration] or [ individual(self.problem,self,solution, self.problem.objectiveScores(solution)) for solution in self.problem.randomSample(self.np)]
        self.baselineGeneration=currentGeneration[::]
        g=0
        lives=1
        while lives > 0:
            lives-=1
            lastGeneration=currentGeneration[::]
            for i,ind in self.selection(currentGeneration):
                participants = self.extrapolationParticipantPairs(ind.solution, currentGeneration)
                newIndividual = self.extrapolate(ind,participants, cf, f)
                currentGeneration[i]= newIndividual if newIndividual.dominates(ind) else ind
                # Observation : Some times continuousDomination gives one result which is not right if we consider infamous sum as the dominace criteria.
            lives=self.problem.krallbstopmethod(lives,lastGeneration,currentGeneration)
            print("Generation ",g+1,'/',g+lives, currentGeneration)
            g+=1

            # if  sum([self.score(self.problem.objectiveScores(solution)) for solution in nextGeneration])/np > (1-epsilon):
            #     break
        print('\n Pareto Frontier -',paretoFrontier)
        self.results=paretoFrontier


class deb2(de):
    """DE/best/2
    Xbest + F* ( A + B -Y -Z)
    """
    def __init__(self):
        pass

class dertob1(de):
    def __init__(self):
        pass

class dec1(de):
    def __init__(self):
        pass

class decd1(dec1):
    def __init__(self):
        pass

class deco1(dec1):
    def __init__(self):
        pass


"""
MIT License

Copyright (c) 2016 Neela Krishna Teja Tadikonda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from __future__ import division
from bisect import bisect
from utils import Pretty
from math import pi

def median(population, isSorted=False):
	population=population if isSorted else sorted(population)
	l=len(population)
	if l%2 == 1: return (population[l//2],population[(l//2)+1])
	return population[l//2]

def mean(population):
	return sum(population)/len(population)

def cohens(p1,p2):
	delta=p1.mean-p2.mean
	combinedPopulation=p1.extend(p2)
	if delta >= 0.3*combinedPopulation.standardDeviation:
		return "large effect"
	elif 0.1*combinedPopulation.standardDeviation <= delta < 0.3*combinedPopulation.standardDeviation:
		return "medium effect"
	return "small effect"

def hedges():
	pass


def a12slow(p1,p2,small=0.56):
	greaterCount=equalCount=0
	for p1i in p1:
		for p2i in p2:
			if p1i == p2i:  equalCount+=1
			elif p1i > p2i: greaterCount+=1
	return (greaterCount+ 0.5*equalCount)/(len(p1)+len(p2))  < small

def cliffsDelta(p1,p2, small=0.147):
	greaterCount=lesserCount=0
	for p1i in pi.sorted:
		for p2i in pi.sorted:
			if p1i < p2i:  lesserCount+=1
			elif p1i > p2i: greaterCount+=1
	return (greaterCount+ 0.5*lesserCount)/(p1.size+p2.size)  < small


def compare(population1,population2):
	p1m,p2m=median(population1),median(population2)

def percentile(percentilevalue,rawvalues=None,normalisedValues=None):
	sortedrawvalues=None
	if not normalisedValues:
		sortedrawvalues=sorted(rawvalues)
		width=sortedrawvalues[-1]-sortedrawvalues[0]
		normalisedValues=[(v-sortedrawvalues[0])/width for v in rawvalues]

	print sortedrawvalues
	print normalisedValues
	cutpoints=[0.1,0.3,0.5,0.7,0.9]
	print [ (sortedrawvalues[bisect(normalisedValues, cp)-1],bisect(normalisedValues, cp),cp)  for cp in cutpoints ]


class bootstrap(Pretty):

	def __init__(self,population1,population2):
		self.population1,self.population2=population1,population2
		self.combinedPopulation=[]
		self.combinedPopulation.extend(self.population1)
		self.combinedPopulation.extend(self.population2)
		self.delta=self.testStatistic(self.population1,self.population2)

	def testStatistic(self, population1, population2):
		delta=population2.mean - population1.mean
		if population1.standardDeviation+population2.standardDeviation:
			delta/=((population2.standardDeviation/len(population1))+(population2.standardDeviation/len(population2)))**0.5
		return delta

	def run(self, conf=0.1,repeats=10):
		count=0
		for _ in xrange(repeats):
			if self.testStatistic(newpopulation1.sampleWithReplacement(),newpopulation2.sampleWithReplacement()) > self.delta:
				count+=1
		return count/repeats < conf
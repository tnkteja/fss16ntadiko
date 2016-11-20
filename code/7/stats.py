from __future__ import division
from bisect import bisect

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
	for p1i in pi.sorted:
		for p2i in pi.sorted:
			if p1i == p2i:  equalCount+=1
			elif p1i > p2i: greaterCount+=1
	return (greaterCount+ 0.5*equalCount)/(p1.size+p2.size)  < small

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

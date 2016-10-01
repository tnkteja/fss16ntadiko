#!/usr/bin/python
# -*- coding: utf8 -*-

import random, time

g1 = lambda x1,x2:    x1+x2 >= 2
g2 = lambda x1,x2:    x1+x2 <= 6
g3 = lambda x1,x2:    x1-x2 >= 2
g4 = lambda x1,x2:    (3*x2) - x1 >= 2
g5 = lambda x3,x4:    ((x3-3)**2) + x4 <= 4
g6 = lambda x5,x6:    (x5-3)**2 + x6 - 4

x1x2x6bounds = xrange(0,11)
x3x5bounds = xrange(1,6)
x4bounds = xrange(0,7)

xbounds = [x1x2x6bounds,x1x2x6bounds,x3x5bounds,x4bounds,x3x5bounds,x1x2x6bounds]
f1 = lambda x1,x2,x3,x4,x5:  -(25*(x1-2)**2 + (x2-2)**2 + ((x3-1)**2)*((x4-4)**2)+(x5-1)**2)
f2 = lambda x1,x2,x3,x4,x5,x6:  x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2

solutions=[]
f1s=[]
f2s=[]
randomsolution = lambda:    [ random.sample(bounds,1)[0] for bounds in xbounds]
for i in xrange(100):
	sol= tuple(randomsolution())
	if sol not in solutions:
		solutions.append(sol)
	f1s.append(f1(*sol[:-1]))
	f2s.append(f2(*sol))
# print solutions
# print f1s
# print f2s
agg=map(lambda x1,x2:  x1+x2, f1s,f2s)

mascore=max(agg)
miscore=min(agg)

score = lambda x1,x2,x3,x4,x5,x6:  f1(x1,x2,x3,x4,x5)+f2(x1,x2,x3,x4,x5,x6)
def MaxWalkSat(threshold,maxtries=20,maxchanges=50,p=0.5):
	solb=None
	out='#'*3+" mwsDemo "+'#'*20 +'\n'
	out+='# '+time.ctime()
	out+="# Basic Study\n"
	out+="!!! Osyczka2\n\n"
	for i in xrange(maxtries):
		out+="Retry %.2d"%(i)+' : '
		sol = randomsolution()
		for j in xrange(maxchanges):
			sol = solb or sol
			sol=list(sol)
			if score(*sol) < -2000:
				print "rvt",score(*sol),threshold
				return sol
			c = random.sample(xrange(6), random.randint(1,6))
			randomsetting=random.choice(c)
			out+=str(randomsetting)
			# At some probability jump around
			if p < random.random():
				for k in c:
					randomsettingvalue = random.choice(xbounds[randomsetting])
					sol[randomsetting] = randomsettingvalue
				out+='?'
			# Then, at probability (1-p), fixate on one variable and try all its 
			# values in (say) increments of (max-min)/10 (and use the value that most 
			# improves the score function).
			else:
				miscore=score(*sol)
				misol=tuple(sol)
				for k in xbounds[randomsetting]:
					sol[randomsetting]=k
					s=score(*sol)
					miscore,misol =  (s,tuple(sol)) if s < miscore else (miscore,misol)
				solb=misol
				out+='!'
		out+='\n'
			# If you couldn't find a better solution, retry again.
	out+="\n Solution : "+ ','.join(map(str,solb))+", Score : "+str(miscore)
	out+="\n\n Copyright 2016, Neela Krishna Teja Tadikonda"
	print out
	

MaxWalkSat(-1)


# -*- coding: utf8 -*-
from __future__ import print_function, division

__all__= None
__author__ = "Neela Krishna Teja Tadikonda"
__version__ = 0.1

import time,random

print('#'*3+" saDemo "+'#'*25)
print('#',time.ctime())
print("# Basic study")
print("!!! Schaffer")
print()
print("Schaffer")
f1=lambda x:  x**2

f2=lambda x:  (x-2)**2
K=1000
sign=lambda x:  x/abs(x)

def neighbour(x):
	X=x+(random.randint(1, 1000) * (1 if random.random() < 0.5 else -1))
	while  -10**5 < X and X > 10**5:
		X=x + (random.randint(1, 1000) * (1 if random.random() < 0.5 else -1))
	return X

prerunresults = [  f1(x) + f2(x) for x in random.sample(xrange(-10**5+1, 10**5-1), 100)]
ma = max(prerunresults)
mi = min(prerunresults)
energy = lambda x:   (f1(x)+f2(x)-mi)/(ma-mi)
emax = 1
x0=random.randint(-10**5+1, 10**5-1)
k=K
x,e=x0,energy(x0)
xb,eb=x0,e
prob = lambda e,en,k:  k

while 0<k<=K and e < emax:
	if k%25 ==0:
		print(", %.4d "%(1000-k),end='')
	#I am choosing a neighbour to jump
	xn=neighbour(x)
	#This neighbour gives me some energy
	en=energy(xn)
    #If the new energy I found is better than what I found so far, let me update
    # my best solution variables and keep them with me.
	if en > eb:
		xb,eb=xn,en
		print('!',end='')
	#If the new energy I found is less than the last energy I found, I need to do better
	if en < e:
		x,e=xn,en
		print('+' ,end='')
	#If I did a better move and my temp is high, high prob jumping from your new solution
	elif prob(e,en,k/K) > random.random():
		x,e=xn,en
		print('?',end='')
	print('.',end='')
	k-=1
	print('\n' if k%25 ==0 else '',end='')

print()
print(eb,xb,emax)

print()
print('-'*36,end='')
print()
print("© 2016 MIT, Neela Krishna Teja Tadikonda")

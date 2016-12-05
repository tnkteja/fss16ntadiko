from pickle import load
from collections import defaultdict
from itertools import combinations
from pprint import pprint
from stats import median, a12slow
from borrowed.borrowed import bootstrap
from time import clock

dic=None
with open("lossStatisics.pickle","r") as f:
	dic=load(f)


items=dic.items()
items.sort(key=lambda t:  median(t[1][0]))
pprint(items)

with open("populations.txt",'w') as f:
    for k,vs in items:
        print >> f,k
        print >> f,' '.join(map(str,vs[0]))
        print >> f, ''

quit()
print "Median Performance Scores Comparision by ranking:\n\t",'\n\t'.join(map(lambda t: str(t[0])+" "+str(median(t[1][0]))+" "+str(t[1]) ,items))

print "Checking for small effects - a12(slow)"
for one, other in combinations(items,2):
	boolean=a12slow(one[1][0], other[1][0])
	print "\t Different ?",one[0],"and",other[0],"is",boolean

start=clock()
print "Checking Hypothesis test - bootstrap for significantly Different"
for one, other in combinations(items,2):
	boolean=bootstrap(one[1][0], other[1][0])
	print "\t Different ?",one[0],"and",other[0],"is",boolean

print "Bootstrap takes time",clock()-start
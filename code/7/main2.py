from pickle import load
from collections import defaultdict
from itertools import combinations

from stats import median, a12slow

dic={"mwse":[6407, 6187, 6885, 6892, 6401, 7302, 6848, 6471, 6574, 6159, 5856, 6406, 6512, 6674, 7317, 6099, 6371, 6559, 7380, 5992],
"sae":[6209, 6215, 6404, 6799, 6764, 7127, 6431, 5677, 6259, 6118, 5796, 6104, 6371, 6379, 7086, 6155, 6179, 5744, 7109, 5985],
"de": [5482,5595,7212,5468,7061,5611,5321,5530,5495,5639,5547,5462,5568,5593,5590,7234,5435,5282,8445,5623]}

items=dic.items()
items.sort(key=lambda t:  median(t[1]))

with open("populations.txt",'w') as f:
    for k,vs in items:
        print >> f,k
        print >> f,' '.join(map(str,vs))
        print >> f, ''

print "Median Performance Scores Comparision by ranking:\n\t",'\n\t'.join(map(lambda t: str(t[0])+" "+str(median(t[1]))+" "+str(t[1]) ,items))

print "Checking for small effects"
for one, other in combinations(items,2):
	boolean=a12slow(one[1], other[1])
	print "\t Small effect between",one[0],"and",other[0],"is",boolean

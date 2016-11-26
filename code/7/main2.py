from pickle import load
from collections import defaultdict

from stats import median
from stats import a12slow
from  

dic={"mwse":[6407, 6187, 6885, 6892, 6401, 7302, 6848, 6471, 6574, 6159, 5856, 6406, 6512, 6674, 7317, 6099, 6371, 6559, 7380, 5992],
"sae":[6209, 6215, 6404, 6799, 6764, 7127, 6431, 5677, 6259, 6118, 5796, 6104, 6371, 6379, 7086, 6155, 6179, 5744, 7109, 5985]}

items=dic.items()
items.sort(key=lambda t:  median(t[1]))
print "Median Performance Scores Comparision by ranking:\n\t",'\n\t'.join(map(lambda t: t[0],items))

print "Checking for small effects"
for i in xrange(1):
	boolean=a12slow(items[i][1], items[i+1][1])
	print "\t Small effect between",items[i][i],"and",items[i+1][0],"is",boolean

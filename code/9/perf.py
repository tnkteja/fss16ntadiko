from pickle import load
from problems import kursawe
from optimizers import sae,de

p=kursawe(optimizer=de())
with open("kursawe_de.pickle","rb") as f:
	kursawe_de=load(f)
p.makeReferenceSetScores(kursawe_de, limitTo=100)
print len(p.referenceSet)
print ','.join(map(str,[p.interGenerationalDistance(kursawe_de[i], p.referenceSet) for i in xrange(20)]))

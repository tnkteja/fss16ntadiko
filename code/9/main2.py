from pickle import load


dic=None
with open("nsga2lossStatistic.pickle",'r') as f:
    dic=load(f)

items=dic.items()

with open("statsX.txt",'w') as f:
    for k,vs in items:
        print >> f,'' 
        print >> f,k
        print >> f,' '.join(map(str,vs[0]))

    


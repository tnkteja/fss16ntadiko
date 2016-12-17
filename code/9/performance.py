from itertools import chain

def spread(df,dl,ds,dbar,N):
	"""
	Spread is also known as diversity. We need less spread of each point to its neighbour.
	"""
	return (df+dl+sum(map(lambda x:  abs(x-dbar),ds)))/(df+dl+(N-1)*dbar)


def bd(objective,other,better=lambda x,y:  x<y):
	atleastone=False
	for i,v in enumerate(objective):
		if better(v,other[i]):
			atleastone=True
		elif v!=other[i]:
			return False
	return atleastone

def make_reference_set(*solutions,better=bd,size=20):
	"""
	Take the optimized solutions sets for the problem and make a reference set for them.
	We can use
	"""
	solutions=chain(*solutions)
	fitness = lambda x:  len(filter(lambda x:  better(solution,x), solutions)) # here we are wasting one calculation when we are inputting same solution for bd.
	return map(lambda solution:  (solution,fitness(solution)), solutions)[:size]
	

def igd(optimizedSolutions, optimizedReferenceSolutions):
	"""Intergenerational Distance
	Problem1: Optimal reference set may be unobtainable (if the model is very nasty).

	Solution1: Let every optimizer work on populations of size "N"
	Let the combined Pareto frontier from "a" optimizers, removing duplicates.
	Down select those "aN" items to the the best "N" best ones.
	Use the resulting space as the reference set
	Problem2: How to remove duplicates?

	Solution2a: exact match on decisions (may not be v.useful for real-valued decisions)
	Solution2b: from the business users, find the minimum value ε that they can control each decision. Declare two decisions same if they are within ε.
	Problem3: How to down select?

	Solution3: count how many times each item in "aN" dominates something else.
	Keep just the "N" items with highest domination count.
	Problem3a: with binary domination, many things may have the highest domination count, especially when dealing with high dimensional objections.

	Solution 3a1: Delete at random from most crowded parts of the Pareto frontier. Why? Cause in crowded spaces, many decisions give rise to the same objective scores.
	Solution 3a2: Don't use binary domination. Instead, use continuous domination since, usually, cdom rejects one item in the comparison. So in this approach, sort each item by the sum of how much it losses to everyone else. They pick the "N" that lose least.
	Problem 3a1a: How to compute "crowded"

	Select all candidates that dominate the most number of other candidates.
	For that set, sort each candidate separately on each objective.
	On each objective Oi, compute the distance left and right to its nearest neighbor
	Let the cuboid around a candidate Vx be the product Vx = ∏iOi
	Sort the candidates descending by Vx.
	Return the left-most "N" items in that sort.
	"""
	
	pass



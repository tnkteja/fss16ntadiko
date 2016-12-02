| problem    | GA Parameters (Mutation, Crossover, Select, Size, Generations)   |
|:-----------|:-----------------------------------------------------------------|
| dtlz1.10.2 | (0.5, 'uniform', 'continuousDominanceLoss', 50, 80)              |
| dtlz1.20.2 | (0.3, 'TwoPoint', 'dominanceCount', 50, 80)                      |
| dtlz1.40.2 | (0.5, 'TwoPoint', 'dominanceRank', 50, 80)                       |
| dtlz1.10.4 | (0.3, 'TwoPoint', 'dominanceRank', 50, 80)                       |
| dtlz1.20.4 | (0.3, 'uniform', 'continuousDominanceLoss', 50, 80)              |
| dtlz1.40.4 | (0.5, 'TwoPoint', 'dominanceRank', 50, 80)                       |
| dtlz1.10.6 | (0.5, 'singlePoint', 'continuousDominanceLoss', 50, 20)          |
| dtlz1.20.6 | (0.1, 'TwoPoint', 'dominanceCount', 50, 80)                      |
| dtlz1.40.6 | (0.3, 'singlePoint', 'continuousDominanceLoss', 50, 40)          |
| dtlz1.10.8 | (0.1, 'TwoPoint', 'dominanceCount', 50, 80)                      |
| dtlz1.20.8 | (0.1, 'singlePoint', 'dominanceRank', 50, 20)                    |
| dtlz1.40.8 | (0.3, 'TwoPoint', 'dominanceCount', 50, 40)                      |
| dtlz3.10.2 | (0.3, 'singlePoint', 'continuousDominanceLoss', 50, 20)          |
| dtlz3.20.2 | (0.1, 'uniform', 'dominanceRank', 50, 40)                        |
| dtlz3.40.2 | (0.3, 'TwoPoint', 'dominanceCount', 50, 80)                      |
| dtlz3.10.4 | (0.1, 'singlePoint', 'dominanceCount', 50, 20)                   |
| dtlz3.20.4 | (0.1, 'singlePoint', 'dominanceRank', 50, 20)                    |
| dtlz3.40.4 | (0.5, 'uniform', 'dominanceRank', 50, 80)                        |
| dtlz3.10.6 | (0.1, 'uniform', 'dominanceCount', 50, 20)                       |
| dtlz3.20.6 | (0.3, 'TwoPoint', 'continuousDominanceLoss', 50, 80)             |
| dtlz3.40.6 | (0.1, 'singlePoint', 'continuousDominanceLoss', 50, 40)          |
| dtlz3.10.8 | (0.3, 'uniform', 'dominanceCount', 50, 40)                       |
| dtlz3.20.8 | (0.5, 'uniform', 'dominanceCount', 50, 80)                       |
| dtlz3.40.8 | (0.3, 'uniform', 'dominanceCount', 50, 20)                       |
| dtlz5.10.2 | (0.5, 'TwoPoint', 'continuousDominanceLoss', 50, 20)             |
| dtlz5.20.2 | (0.3, 'singlePoint', 'continuousDominanceLoss', 50, 40)          |
| dtlz5.40.2 | (0.5, 'TwoPoint', 'dominanceRank', 50, 80)                       |
| dtlz5.10.4 | (0.3, 'TwoPoint', 'continuousDominanceLoss', 50, 20)             |
| dtlz5.20.4 | (0.1, 'singlePoint', 'dominanceCount', 50, 80)                   |
| dtlz5.40.4 | (0.3, 'singlePoint', 'continuousDominanceLoss', 50, 40)          |
| dtlz5.10.6 | (0.1, 'TwoPoint', 'continuousDominanceLoss', 50, 80)             |
| dtlz5.20.6 | (0.3, 'uniform', 'dominanceCount', 50, 40)                       |
| dtlz5.40.6 | (0.3, 'TwoPoint', 'continuousDominanceLoss', 50, 20)             |
| dtlz5.10.8 | (0.3, 'singlePoint', 'dominanceCount', 50, 40)                   |
| dtlz5.20.8 | (0.1, 'TwoPoint', 'dominanceCount', 50, 80)                      |
| dtlz5.40.8 | (0.5, 'TwoPoint', 'continuousDominanceLoss', 50, 40)             |
| dtlz7.10.2 | (0.1, 'uniform', 'dominanceCount', 50, 80)                       |
| dtlz7.20.2 | (0.3, 'singlePoint', 'dominanceCount', 50, 40)                   |
| dtlz7.40.2 | (0.3, 'TwoPoint', 'continuousDominanceLoss', 50, 40)             |
| dtlz7.10.4 | (0.3, 'TwoPoint', 'continuousDominanceLoss', 50, 80)             |
| dtlz7.20.4 | (0.1, 'singlePoint', 'dominanceCount', 50, 80)                   |
| dtlz7.40.4 | (0.3, 'uniform', 'continuousDominanceLoss', 50, 40)              |
| dtlz7.10.6 | (0.1, 'singlePoint', 'continuousDominanceLoss', 50, 40)          |
| dtlz7.20.6 | (0.1, 'uniform', 'dominanceRank', 50, 20)                        |
| dtlz7.40.6 | (0.3, 'singlePoint', 'continuousDominanceLoss', 50, 40)          |
| dtlz7.10.8 | (0.3, 'TwoPoint', 'continuousDominanceLoss', 50, 20)             |
| dtlz7.20.8 | (0.3, 'singlePoint', 'dominanceRank', 50, 20)                    |
| dtlz7.40.8 | (0.3, 'singlePoint', 'continuousDominanceLoss', 50, 80)          |

# Homework 7 - Early Termination - Learning when enough is enough.

___Not we ___

_keywords: optimization, random, searching_


## Introduction
Not all problems are easy to solve using simple deterministic algorithms. More often than not we have problems for which we make some decisions and end up with some quantitative results, which are our objectives, all as a consequence of our choices for those decisions. But the lingering question for anyone is how to manage their decisions so that they get gain margin over the set of objectives they care for. This spawns them with several more questions, on whether they can have good number of optimal solutions, useful in making practical decisions. Such optimal solutions are achieved by random searching or unordered searching. Ordered searching requires us to make tricky decisions when choosing next decision or set of decisions in the series of decisions we make, but unordered search does not assume any knowledge. It is rich with possibilities and might give good insights into the uncharted territory which is otherwise dark using the ordered search using deterministic algorithms.Random searching for solution rigorously seems a naive brute-force way to solve the problem, it takes no assumptions of the kind of problem and is also not guaranteed to provide a best solution. But more often than not these optimizing random search provides close to real solutions, by using some techniques in the way of searching. These random searches also known as stochastic searches, take advantage of the todays CPU speeds, and memory access speeds and other state of the art chip technologies used to built todays computing devices.

Most of the algorithms that perform the unordered search do the mutation on the set of decisions to randomly traverse over the solution space. Mutation is a operation, which is changing the part of the solution, which as mentioned earlier contains set of decisions. Two identifiable trends can be understood when we look at the algorithms that perform unordered search, namely local search and stochastic search. Local search involves mutating a part of the solution such that we achieve optimal objectives with the this search. Stochastic search as the name says, is a straight forward - mutation and search paradigm, where we perform mutation, look the objective for this solution and keep searching.



## Related Work
The optimizing algorithms dates back to the 1950's when the memory of the computer was so little and CPU processing speeds were not very impressive when compared to the modern day's computing devices.  Simulated annealing is an approach used to find optimal solutions for single objective problems with only as little memory as maintaining 3 variables at any given time which are - current solution - best solution - next solution. Simulated annealing runs over several iterations and is known to given a close to optimal solution at the end of the iterations [1].
Doing only local search does not always guarantee us of the optimal solution often needs to jump across the local search into stochastic search to cover the landscape of the outcomes from the solution space. Quite popular as this philosophy is, there is a stochastic algorithm called MaxWalkSat, which is non-parametric stochastic method for sampling the landscape of a local region. [2]


We have few performance scores like Hypervolume, Intergenerational Distance, and Spread, to measure how well did the optimizer do with the problem. This performace measures can also be used to compare various optimizers on a given problem.



## The Body 2-4 main sections

For the design challenge, we pick the performace meassure IGD to compare the optmizers Simulated Annealng, Max Walk Sat, and DE against each other on a common problem.


* _Type 1 Comparision Opeartor_ It is used to decide if an individual of the population is better than another individual.

* _Type 2 Comparision Operator_ It is used to find if there is any improvement from the last generation to the current generation.

* _Type 3 Comparision Operator_ It is used to to compare two optimizers on their performace with the problem they performed optimization on. For example Hypervolume, Spread, IGD.

## Performance Experiments
In this report we run the optimizers - Simulated Annealing, Max Walk Sat and Differential Evolution on ...

## The Conclusions

## Future Work

## The Acknowledgments

___References:___

1.  _S. Kirkpatrick and C. D. Gelatt and M. P. Vecchi Optimization by Simulated Annealing, Science, Number 4598, 13 May 1983, volume 220, 4598, pages 671680,1983._

2.  _Kautz, H., Selman, B., & Jiang, Y. (n.d.). A General Stochastic Approach to Solving Problems with Hard and Soft Constraints, 0, 1–14._

## Appendices
### Grammar and Small-Scale Presentation Issues
### Mechanics
### Versions and Distribution

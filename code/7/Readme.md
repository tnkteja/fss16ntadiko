# Homework 7 - Early Termination - Learning when enough is enough.

___Not w ___

_keywords: optimization, random, searching_


## Introduction
Not all problems are easy to solve using simple deterministic algorithms. More often than not we have problems for which we make some decisions and end up with some quantitative results, which are our objectives, all as a consequence of our choices for those decisions. But the lingering question for anyone is how to manage their decisions so that they get gain margin over the set of objectives they care for. This spawns them with several more questions, on whether they can have good number of optimal solutions, useful in making practical decisions. Such optimal solutions are achieved by random searching or unordered searching. Ordered searching requires us to make tricky decisions when choosing next decision or set of decisions in the series of decisions we make, but unordered search does not assume any knowledge. It is rich with possibilities and might give good insights into the uncharted territory which is otherwise dark using the ordered search using deterministic algorithms.Random searching for solution rigorously seems a naive brute-force way to solve the problem, it takes no assumptions of the kind of problem and is also not guaranteed to provide a best solution. But more often than not these optimizing random search provides close to real solutions, by using some techniques in the way of searching. These random searches also known as stochastic searches, take advantage of the todays CPU speeds, and memory access speeds and other state of the art chip technologies used to built todays computing devices. 

Most of the algorithms that perform the unordered search do the mutation on the set of decisions to randomly traverse over the solution space. Mutation is a operation, which is changing the part of the solution, which as mentioned earlier contains set of decisions. Two identifiable trends can be understood when we look at the algorithms that perform unordered search, namely local search and stochastic search. Local search involves mutating a part of the solution such that we achieve optimal objectives with the this search. Stochastic search as the name says, is a straight forward - mutation and search paradigm, where we perform mutation, look the objective for this solution and keep searching.



## Background
The optimizing algorithms dates back to the 1950's when the memory of the computer was so little and CPU processing speeds were not very impressive when compared to the modern day's computing devices.  Simulated annealing is an approach used to find optimal solutions for single objective problems with only as little memory as maintaining 3 variables at any given time which are - current solution - best solution - next solution. Simulated annealing runs over several iterations and is known to given a close to optimal solution at the end of the iterations [1].
Doing only local search does not always guarantee us of the optimal solution often needs to jump across the local search into stochastic search to cover the landscape of the outcomes from the solution space. Quite popular as this philosophy is, there is a stochastic algorithm called MaxWalkSat, which is non-parametric stochastic method for sampling the landscape of a local region. [2] Diffrentia Evolution is another algorithm which banks on the idea that when sampling decisions from a distribution is unknown, it can be derived from the latest frontier itself, by extrapolation and slight mutation - which is usually to find a better variant.


We have few performance scores like Hypervolume, Intergenerational Distance (IGD), and Spread, to measure how well did the optimizer do with the problem. This performace measures can also be used to compare various optimizers on a given problem. While these performance measures are good for multi-objective optimiztions with one or more or none competing objectives. The historical optimizer algorithms like SA, MWS, DE can use the traditional aggregate sum or Continuous Dominance Loss as performance measures. The more hypervolume tells that a optimizer has worked its way more towards the utopia and gives betters results. Spread is another measure that is provding a quick view of the spread between the objectives achived in the final frontier. Intergenerational dstance tells us


## Early Termination

The algorithms can run for a long periods but not showing improvement of the results so far it generated. It is necessary to identify a good set of satisfactory results and terminate the algorithm when it reaches that. Terminating early saves a lot of time when we are looking for solutions which are better, not always best. A early termination criteria is coded up in each of the algorithms to recognise no improvement of results. Although early stopping criteria can be achieved in several ways like

1.  Assume a budget of computations, and terminate the optimizer when we hit that budget.

2. After each era of computations( era begin a significant number of computations which can perhaps be used as an unit), we can measure the improvement on the last era, we can push for another x( used 5 ) eras, if we find an improvement, or  reduce the number eras currently under immediate consideration. 

For the design challenge, we pick the performace meassure IGD to compare the optmizers Simulated Annealng, Max Walk Sat, and DE against each other on a common problem.


## Comparision Operators

While we code or analyse these optimizing algorithms we come across of identify the need for the following Comparision operators. 

* _Type 1 Comparision Opeartor_ It is used to decide if an individual of the population is better than another individual. The way an individual dominates another can be an aggregate function, which is nothing but a 
  * weighted objective sores sum Or
  * a binary domination,
  * and continuous domination.

* _Type 2 Comparision Operator_ It is used to find if there is any improvement from the last generation to the current generation. We can use any performance measure that  provides insight into the difference in improvement from last generatino to current generation. Some operators are
  * Using type 1 compator and  determining improvement if atleast x (say 1) improvements in last generation or era, e.t.c

  * Using performance measure of multi-objective optimizers like IGD, Spread, or Continuous Dominance Loss. 

* _Type 3 Comparision Operator_ It is used to to compare two optimizers on their performace with the problem they performed optimization on. Some performance measures are
  * Hypervolume,
  * Spread,
  * IGD
  * Continuous Dominance Loss

### Continuous Dominance Loss

As mentioned earlier we type 3 comaprision for evaluating the performance of the optimizers. Contiuous Dominance is another parameter bsaed on the continuous dominance value alculated between two individuals. For each individual in first generation we add the loss he makes on all the individuals in the final generation, then we add all the losses made by all te individuals in the first generation.

## Evaluation

We generate the baseline populations and freeze them to disk immedietely after conceiving the problem. These same baseline populations are used for various runs of the optimizers, making sure that all runs of the differentt optimizers run on same set of baseline populations. 

1. We generate 20 baseline generations each with 100 in size.

2. SA, MWS is run on each of individual in the first generation and a final generation is evaluated, which is the best solution from each run. Although an alternate approach is to seed one solution and capture a frontier along with the best solution is feasible, we think the earlier ways makes it a good candidate with the fellow frontier kind optimizers like DE.

3. DE works on frontiers so we take the first geenration of individuals as a frontier and work on them. 

4. Since the _Type 2_ comparators  are coded up into the optimizers, where we used the incrementally push for eras approach for early,termination, the optmizers ran accordingly and terminated early.

5. We finally calulate the Continuous dominance loss of each baseline population for each optimizer, so we get 20 values of SA, MWS and DE, which then are subjected to statistical tests for the comaprision.

## Results and Discussion

The optimizers are run over 20 baseline poupulations each baslinepopulation with 100 individuals. After the optimizers run over these populations we get 20 performance score for each baseline populations, for each optimizer. Now these optimizers need to be compared and we performed follwing comparisions.

First we rank the optimizers using the MEDIAN Performance scores, which is the preferred central tendency for comparisions. We observe that DE is doing better amoung 3 of them followed by sa, and mws. We then perform to see effect size test between these performance scores as follows. Since this is dominance loss, the more loss the better the optimizer is so ***MWS is doing better than SA and DE***.

![results.png](https://rawgit.com/tnkteja/fss16ntadiko/hw7/code/7/.images/results.png)

The above results show that the median performance scores comparisions for the performace parameter continuous dominance loss. 

We then continue to perform the Effect size tests on the above performance populations. We use the non-parametric test a12 to determine the effect size tests. The results show that DE and SA is Small Effect, but other two combinations DE and MWS, SA and MWS are significantly different.

We also perform the Hypothesis test - bootstrap, and the results same as the results from the effect size tests. We configured bootstrap for 10000 runs and it takes 16 seconds to complete the test.

Additionally we perform the scottknott test to validate our results and scott knott gives the same set of results as we derived.

![scottknott](https://rawgit.com/tnkteja/fss16ntadiko/hw7/code/7/.images/sk.png)

## Threats to Validity

There are several validity threats to the design of this study. Our choice of venue is limited to a single venue and a single year. In extending this work we should of course include more venues and more years. This would both give more data and allow better and more detailed statistical analysis as well as allowing a broader coverage of the field of software engineering. Care should be taken to ensure that also quality studies are found and included. During data collection we mostly used a single researcher to review each paper. Although we tried to mitigate this threat by noting any unclear issues and discuss them together there is still a higher risk that a single reviewer can be biased and consistently extract the wrong information. For the future we hope to have the resources to have at least two reviewers for each paper. The pilot with co-review of four papers should have helped to create a common understanding though. Another threat to the data collection is that our chosen categories did not always fit the papers, threats and/or mitigation strategies. Based on the experience from this initial survey we will update the form further to ensure consistent collection and analysis of results. We see few threats to the numerical analysis, however there are several threats to the analysis of the threat and strategy summaries. Since we had no unified framework with which to classify the threats or strategies our analysis at this stage is only indicative; without statistics on which threats are common and not the analysis is unreliable.

## Future Work

* The early termination critera can be fine tuned to see if for a problem a parameter used in the early termination criteria can give good enough resutls within very resonable time. For example instead pushing for 5 more eras, we can push for 8 eras and reduce by 2 eras when we find no improvements. 

* In DE, the early termination criteria, instead of using KrallsBStop method, a same approach used in the earlier methods can be used to see if we find a better solution than the best solution in the last era, which is an improvement and then push for another 5 eras.

*


## The Acknowledgments

We thank Dr. Menzies for the statistical machinery code for scottknott, bootstrap, a12, cohens e.t.c shared with us for the class homework projects.[6]

___References:___

1.  _S. Kirkpatrick and C. D. Gelatt and M. P. Vecchi Optimization by Simulated Annealing, Science, Number 4598, 13 May 1983, volume 220, 4598, pages 671680,1983._

2.  _Kautz, H., Selman, B., & Jiang, Y. (n.d.). A General Stochastic Approach to Solving Problems with Hard and Soft Constraints, 0, 1–14._

3. _Deb, K., Thiele, L., Laumanns, M., Zitzler, E., Abraham, A., Jain, L., & Goldberg, R. (2005). Scalable test problems for evolutionary multiobjective optimization. Evolutionary Multiobjective, (1990), 1–27. http://doi.org/10.1007/1-84628-137-7_

4. _Timm Menzies. https://github.com/txt/mase/blob/master/lessthan.md_

5. _Timm Mezies. https://github.com/txt/ase16/blob/master/doc/stats.md_

6. _Timm Mezies. https://github.com/txt/ase16/blob/master/src/stats.py_

6. Andrea Arcuri and Lionel Briand. 2011. A practical guide for using statistical tests to assess randomized algorithms in software engineering. In Proceedings of the 33rd International Conference on Software Engineering (ICSE '11). ACM, New York, NY, USA, 1-10. DOI=http://dx.doi.org/10.1145/1985793.1985795


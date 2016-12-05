# Homework 9 - Hyper Parameter Optimization

_keywords: optimization, random, searching_


## Introduction
Not all problems are easy to solve using simple deterministic algorithms. More often than not we have problems for which we make some decisions and end up with some quantitative results, which are our objectives, all as a consequence of our choices for those decisions. But the lingering question for anyone is how to manage their decisions so that they get gain margin over the set of objectives they care for. This spawns them with several more questions, on whether they can have good number of optimal solutions, useful in making practical decisions. Such optimal solutions are achieved by random searching or unordered searching. Ordered searching requires us to make tricky decisions when choosing next decision or set of decisions in the series of decisions we make, but unordered search does not assume any knowledge. It is rich with possibilities and might give good insights into the uncharted territory which is otherwise dark using the ordered search using deterministic algorithms.Random searching for solution rigorously seems a naive brute-force way to solve the problem, it takes no assumptions of the kind of problem and is also not guaranteed to provide a best solution. But more often than not these optimizing random search provides close to real solutions, by using some techniques in the way of searching. These random searches also known as stochastic searches, take advantage of the todays CPU speeds, and memory access speeds and other state of the art chip technologies used to built todays computing devices. 

Most of the algorithms that perform the unordered search do the mutation on the set of decisions to randomly traverse over the solution space. Mutation is a operation, which is changing the part of the solution, which as mentioned earlier contains set of decisions. Two identifiable trends can be understood when we look at the algorithms that perform unordered search, namely local search and stochastic search. Local search involves mutating a part of the solution such that we achieve optimal objectives with the this search. Stochastic search as the name says, is a straight forward - mutation and search paradigm, where we perform mutation, look the objective for this solution and keep searching.


Another set of algorithms came along that are inspired by the Genetic Algorithm, which fundamentally perform crosover and mutatio over a generation of populations. Then prune the less evloved individuals using a process called elitism. This process is called Generation , and we run this for more generation until we get a convergence on the generations. Also we no longer get a single best solution as we have multi-objectives. We look for a optimized frontier called Pareto Frontier, which is the frontier on which all objectives competing and non-competing settle for optimality.

Optimizers can be applied to any problems which can be modelled as decisions and objectives. Which enables us to apply optimizers to diverse set of problems, giving us the opportunity to learn insightful things. 

## Background

Diffrential Evolution is single objctive optimizer, which is fast. It is frnotier based algorithm. We have used homeowor7.

The GA we used so far has the default parameters of 

* with single point crossover,  
* 0.1 mutation rate, 
* 100 individulals in each generation, 
* run for maximum of 100 generations 

These megic number and parameters determine the solutions obtained on the pareto frontier.For example, we may observe improved solution more sooner than later by adjusting the mutation rate. 

### Continuous Dominance Loss

As mentioned earlier we type 3 comaparision for evaluating the performance of the optimizers. Contiuous Dominance is another parameter bsaed on the continuous dominance value alculated between two individuals. For each individual in first generation we add the loss he makes on all the individuals in the final generation, then we add all the losses made by all te individuals in the first generation.

## Evaluation

For each of the problem in DTLZ 2,4,6,8 with decision 10,20,40 we run the GA by variying the magic parameters as

* Mutation over  0.1,0.3,0.5

* Crossover  singlePoint, TwoPoint, uniform

* Select using dominanceCount, dominanceRank, continuousDominanceLoss

* Size over 50,100,150

* Generations  over  20,40,80

using the DE optimizer. As DE optimiers runs using its defaults, we generate each solution which is a set or combination of magi parameters that are initialised into the GA, thus run GA over the same baseline popuations is used to determine the performance parameter for each run as objective. We use CDOMLOSS between first generation and the final generation as the performance parameter. 


## Results and Discussion

Using DE we optimized the magic numbers and parameter for the GA. We obtained the following results.


Problem |GA Parameters (Mutation, Crossover, Select, Size, Generations)
:-:|:-:
dtlz1.10.2|.5, ‘uniform’, ‘continuousDominanceLoss’, 50, 80)
dtlz1.20.2|.3, ‘TwoPoint’, ‘dominanceCount’, 50, 80)
dtlz1.40.2|.5, ‘TwoPoint’, ‘dominanceRank’, 50, 80)
dtlz1.10.4|.3, ‘TwoPoint’, ‘dominanceRank’, 50, 80)
dtlz1.20.4|.3, ‘uniform’, ‘continuousDominanceLoss’, 50, 80)
dtlz1.40.4|.5, ‘TwoPoint’, ‘dominanceRank’, 50, 80)
 dtlz5.40.4|.3, ‘singlePoint’, ‘continuousDominanceLoss’, 50, 40)
dtlz5.10.6|.1, ‘TwoPoint’, ‘continuousDominanceLoss’, 50, 80)
dtlz5.20.6|.3, ‘uniform’, ‘dominanceCount’, 50, 40)
dtlz5.40.6|.3, ‘TwoPoint’, ‘continuousDominanceLoss’, 50, 20)
dtlz5.10.8|.3, ‘singlePoint’, ‘dominanceCount’, 50, 40)
dtlz5.20.8|.1, ‘TwoPoint’, ‘dominanceCount’, 50, 80)
dtlz5.40.8|.5, ‘TwoPoint’, ‘continuousDominanceLoss’, 50, 40)
 dtlz7.10.2|.1, ‘uniform’, ‘dominanceCount’, 50, 80)
dtlz7.20.2|.3, ‘singlePoint’, ‘dominanceCount’, 50, 40)
dtlz7.40.2|.3, ‘TwoPoint’, ‘continuousDominanceLoss’, 50, 40)
dtlz7.10.4|.3, ‘TwoPoint’, ‘continuousDominanceLoss’, 50, 80)
dtlz7.20.4|.1, ‘singlePoint’, ‘dominanceCount’, 50, 80)
dtlz7.40.4|.3, ‘uniform’, ‘continuousDominanceLoss’, 50, 40)
dtlz7.10.6|.1, ‘singlePoint’, ‘continuousDominanceLoss’, 50, 40)
 dtlz7.20.6|.1, ‘uniform’, ‘dominanceRank’, 50, 20)
dtlz7.40.6|.3, ‘singlePoint’, ‘continuousDominanceLoss’, 50, 40)
dtlz7.10.8|.3, ‘TwoPoint’, ‘continuousDominanceLoss’, 50, 20)
dtlz7.20.8|.3, ‘singlePoint’, ‘dominanceRank’, 50, 20)
dtlz7.40.8|.3, ‘singlePoint’, ‘continuousDominanceLoss’, 50, 80)

We can after getting the tuned vs untuned GA run againsts 20 baseline populations and get the statistical analysis results. We find that either ga and tuned ga are doing equally good or tunedga is performing better than ga on cdomloss parameter.

```bash
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.10.2 ,    -19942   ,   35 ( *-----        |              ),-19954.13, -19951.17, -19942.66, -19924.18, -19856.88
   2 , tunedga.0.5.uniform.continuousDominanceLoss.50.80.dtlz1.10.2 ,    -19803   ,  110 (           *   |------------- ),-19838.38, -19830.15, -19803.38, -19744.34, -19564.92

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.20.2 ,    -19991   ,    8 (*-             |              ),-19997.80, -19995.10, -19991.92, -19990.16, -19970.87
   1 , tunedga.0.3.TwoPoint.dominanceCount.50.80.dtlz1.20.2 ,    -19971   ,   30 ( -*------      |              ),-19984.64, -19976.20, -19971.25, -19962.85, -19899.96

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.40.2 ,    -19999   ,    1 (*              |              ),-20000.00, -20000.00, -19999.99, -19999.97, -19999.59
   2 , tunedga.0.5.TwoPoint.dominanceRank.50.80.dtlz1.40.2 ,    -19992   ,   14 (-* ------------|-----------   ),-19996.62, -19993.08, -19992.09, -19980.96, -19846.70

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.10.4 ,    -39844   ,   41 ( - *---        |              ),-39872.70, -39861.00, -39844.36, -39833.98, -39781.83
   2 , tunedga.0.3.TwoPoint.dominanceRank.50.80.dtlz1.10.4 ,    -39649   ,   83 (            -- | *--------    ),-39719.79, -39683.69, -39649.10, -39627.14, -39510.79

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.20.4 ,    -39993   ,    5 (*              |              ),-39996.32, -39995.77, -39993.39, -39990.21, -39983.25
   2 , tunedga.0.3.uniform.continuousDominanceLoss.50.80.dtlz1.20.4 ,    -39874   ,   94 (       -    *  | -----------  ),-39919.60, -39912.93, -39874.52, -39827.42, -39714.32

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.40.4 ,    -39999   ,    0 (*              |              ),-39999.99, -39999.96, -39999.94, -39999.87, -39999.75
   2 , tunedga.0.5.TwoPoint.dominanceRank.50.80.dtlz1.40.4 ,    -39983   ,   22 ( - *  -------  |              ),-39993.71, -39987.86, -39983.34, -39967.02, -39935.37

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.10.6 ,    -59571   ,  101 (   --    *-----|              ),-59684.89, -59638.99, -59571.51, -59555.40, -59464.96
   2 , tunedga.0.5.singlePoint.continuousDominanceLoss.50.20.dtlz1.10.6 ,    -59360   ,  144 (            ---|    * ------  ),-59517.78, -59450.82, -59360.79, -59328.41, -59206.50

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.20.6 ,    -59992   ,    9 (*-             |              ),-59995.46, -59993.96, -59992.12, -59987.70, -59980.12
   2 , tunedga.0.1.TwoPoint.dominanceCount.50.80.dtlz1.20.6 ,    -59922   ,   67 (     -  *    --|-----         ),-59953.35, -59939.71, -59922.19, -59886.14, -59819.14

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.40.6 ,    -59999   ,    0 (*              |              ),-59999.98, -59999.96, -59999.88, -59999.76, -59997.26
   2 , tunedga.0.3.singlePoint.continuousDominanceLoss.50.40.dtlz1.40.6 ,    -59977   ,   32 (- * -----------|------------- ),-59992.02, -59989.24, -59977.67, -59960.47, -59758.62

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.1.TwoPoint.dominanceCount.50.80.dtlz1.10.8 ,    -78845   ,  191 (      ----*----|              ),-79005.81, -78868.21, -78845.36, -78810.63, -78673.10
   2 , ga.dtlz1.10.8 ,    -78267   ,   77 (               |       -- *-- ),-78373.10, -78319.10, -78267.28, -78252.42, -78156.84

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.20.8 ,    -79983   ,   16 (*--            |              ),-79989.10, -79984.23, -79983.45, -79973.42, -79948.24
   2 , tunedga.0.1.singlePoint.dominanceRank.50.20.dtlz1.20.8 ,    -79884   ,   75 (     -- *   ---|---------     ),-79923.94, -79892.46, -79884.55, -79821.70, -79659.71

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz1.40.8 ,    -79999   ,    0 (*              |              ),-79999.95, -79999.92, -79999.79, -79999.48, -79998.08
   1 , tunedga.0.3.TwoPoint.dominanceCount.50.40.dtlz1.40.8 ,    -79968   ,   55 ( *-----        |              ),-79992.99, -79980.94, -79968.74, -79934.78, -79797.38

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.10.2 ,    -19788   ,   64 ( -- *----      |              ),-19838.43, -19806.94, -19788.96, -19774.07, -19697.03
   2 , tunedga.0.3.singlePoint.continuousDominanceLoss.50.20.dtlz3.10.2 ,    -19537   ,  125 (           ----| *---------   ),-19649.52, -19572.42, -19537.74, -19514.59, -19362.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.20.2 ,    -19983   ,   15 ( *--           |              ),-19992.50, -19988.24, -19983.50, -19973.47, -19961.77
   2 , tunedga.0.1.uniform.dominanceRank.50.40.dtlz3.20.2 ,    -19906   ,   71 (     ---   *   | -----        ),-19953.86, -19931.74, -19906.16, -19861.70, -19820.77

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.40.2 ,    -19999   ,    0 (*              |              ),-19999.91, -19999.70, -19999.60, -19999.32, -19996.64
   2 , tunedga.0.3.TwoPoint.dominanceCount.50.80.dtlz3.40.2 ,    -19979   ,   13 (  *--------    |              ),-19990.78, -19985.07, -19979.61, -19976.26, -19911.26

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.10.4 ,    -39507   ,  137 (  ---   *  ----|              ),-39610.39, -39570.03, -39507.08, -39447.68, -39378.12
   2 , tunedga.0.1.singlePoint.dominanceCount.50.20.dtlz3.10.4 ,    -39393   ,  166 (        ---   *|  ----        ),-39510.62, -39456.80, -39393.01, -39314.56, -39233.62

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.20.4 ,    -39981   ,   13 (  *-           |              ),-39990.28, -39987.11, -39981.64, -39978.13, -39968.47
   2 , tunedga.0.1.singlePoint.dominanceRank.50.20.dtlz3.20.4 ,    -39944   ,   38 (     --  *    -|--            ),-39966.66, -39955.98, -39944.85, -39921.39, -39904.09

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.40.4 ,    -39999   ,    1 (*              |              ),-39999.86, -39999.67, -39999.20, -39998.98, -39997.88
   2 , tunedga.0.5.uniform.dominanceRank.50.80.dtlz3.40.4 ,    -39974   ,   23 ( -  *------    |              ),-39989.45, -39986.58, -39974.87, -39968.88, -39939.49

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.10.6 ,    -58927   ,  288 (  -------    * |----          ),-59199.89, -59009.67, -58927.99, -58872.11, -58739.69
   2 , tunedga.0.1.uniform.dominanceCount.50.20.dtlz3.10.6 ,    -58791   ,  330 (      ---------|  *  ------   ),-59102.06, -58873.73, -58791.74, -58722.95, -58574.69

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.20.6 ,    -59951   ,   31 (  *---         |              ),-59969.17, -59967.19, -59951.57, -59939.35, -59910.91
   2 , tunedga.0.3.TwoPoint.continuousDominanceLoss.50.80.dtlz3.20.6 ,    -59821   ,  101 (        -     *| ---------    ),-59888.40, -59871.76, -59821.07, -59784.33, -59686.17

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.40.6 ,    -59999   ,    1 (*              |              ),-59999.77, -59999.67, -59999.43, -59999.05, -59995.51
   2 , tunedga.0.1.singlePoint.continuousDominanceLoss.50.40.dtlz3.40.6 ,    -59908   ,   99 ( - * ----------|-             ),-59963.66, -59937.76, -59908.06, -59844.97, -59539.63

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.10.8 ,    -79370   ,   66 (   - *---      |              ),-79418.99, -79386.15, -79370.97, -79333.22, -79268.30
   2 , tunedga.0.3.uniform.dominanceCount.50.40.dtlz3.10.8 ,    -78998   ,   96 (               |  -- *  ----  ),-79068.77, -79026.50, -78998.37, -78951.82, -78841.85

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.20.8 ,    -79941   ,   20 (-- *           |              ),-79965.84, -79949.75, -79941.68, -79939.63, -79928.99
   2 , tunedga.0.5.uniform.dominanceCount.50.80.dtlz3.20.8 ,    -79755   ,   65 (             --|-    *  ----- ),-79844.37, -79796.23, -79755.79, -79732.28, -79682.43

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz3.40.8 ,    -79998   ,    3 (*              |              ),-79999.69, -79999.24, -79998.65, -79997.72, -79994.42
   2 , tunedga.0.3.uniform.dominanceCount.50.20.dtlz3.40.8 ,    -79968   ,   24 ( -  * ------   |              ),-79988.30, -79980.40, -79968.54, -79958.53, -79920.49

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.10.2 ,    -20000   ,    0 (*              |              ),-20000.00, -20000.00, -20000.00, -20000.00, -20000.00
   1 , tunedga.0.5.TwoPoint.continuousDominanceLoss.50.20.dtlz5.10.2 ,    -20000   ,    0 (*              |              ),-20000.00, -20000.00, -20000.00, -20000.00, -20000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.20.2 ,    -20000   ,    0 (*              |              ),-20000.00, -20000.00, -20000.00, -20000.00, -20000.00
   1 , tunedga.0.3.singlePoint.continuousDominanceLoss.50.40.dtlz5.20.2 ,    -20000   ,    0 (*              |              ),-20000.00, -20000.00, -20000.00, -20000.00, -20000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.40.2 ,    -20000   ,    0 (*              |              ),-20000.00, -20000.00, -20000.00, -20000.00, -20000.00
   1 , tunedga.0.5.TwoPoint.dominanceRank.50.80.dtlz5.40.2 ,    -20000   ,    0 (*              |              ),-20000.00, -20000.00, -20000.00, -20000.00, -20000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.10.4 ,    -40000   ,    0 (*              |              ),-40000.00, -40000.00, -40000.00, -40000.00, -40000.00
   1 , tunedga.0.3.TwoPoint.continuousDominanceLoss.50.20.dtlz5.10.4 ,    -40000   ,    0 (*              |              ),-40000.00, -40000.00, -40000.00, -40000.00, -40000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.20.4 ,    -40000   ,    0 (*              |              ),-40000.00, -40000.00, -40000.00, -40000.00, -40000.00
   1 , tunedga.0.1.singlePoint.dominanceCount.50.80.dtlz5.20.4 ,    -40000   ,    0 (*              |              ),-40000.00, -40000.00, -40000.00, -40000.00, -40000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.40.4 ,    -40000   ,    0 (*              |              ),-40000.00, -40000.00, -40000.00, -40000.00, -40000.00
   1 , tunedga.0.3.singlePoint.continuousDominanceLoss.50.40.dtlz5.40.4 ,    -40000   ,    0 (*              |              ),-40000.00, -40000.00, -40000.00, -40000.00, -40000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.10.6 ,    -60000   ,    0 (*              |              ),-60000.00, -60000.00, -60000.00, -60000.00, -60000.00
   1 , tunedga.0.1.TwoPoint.continuousDominanceLoss.50.80.dtlz5.10.6 ,    -60000   ,    0 (*              |              ),-60000.00, -60000.00, -60000.00, -60000.00, -60000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.20.6 ,    -60000   ,    0 (*              |              ),-60000.00, -60000.00, -60000.00, -60000.00, -60000.00
   1 , tunedga.0.3.uniform.dominanceCount.50.40.dtlz5.20.6 ,    -60000   ,    0 (*              |              ),-60000.00, -60000.00, -60000.00, -60000.00, -60000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.3.TwoPoint.continuousDominanceLoss.50.20.dtlz5.40.6 ,    -60000   ,    0 (*              |              ),-60000.00, -60000.00, -60000.00, -60000.00, -60000.00
   1 , ga.dtlz5.40.6 ,    -60000   ,    0 (*              |              ),-60000.00, -60000.00, -60000.00, -60000.00, -60000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.3.singlePoint.dominanceCount.50.40.dtlz5.10.8 ,    -77926   ,  183 (          -----|   *  ---     ),-78074.30, -77982.33, -77926.54, -77884.52, -77831.00
   1 , ga.dtlz5.10.8 ,    -77923   ,  154 (           ----|   *   --     ),-78060.82, -77975.57, -77923.72, -77868.95, -77828.40

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz5.20.8 ,    -80000   ,    0 (*              |              ),-80000.00, -80000.00, -80000.00, -80000.00, -80000.00
   1 , tunedga.0.1.TwoPoint.dominanceCount.50.80.dtlz5.20.8 ,    -80000   ,    0 (*              |              ),-80000.00, -80000.00, -80000.00, -80000.00, -80000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.5.TwoPoint.continuousDominanceLoss.50.40.dtlz5.40.8 ,    -80000   ,    0 (*              |              ),-80000.00, -80000.00, -80000.00, -80000.00, -80000.00
   1 , ga.dtlz5.40.8 ,    -80000   ,    0 (*              |              ),-80000.00, -80000.00, -80000.00, -80000.00, -80000.00

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.1.uniform.dominanceCount.50.80.dtlz7.10.2 ,    -17882   ,  276 ( -  *--        |              ),-18141.93, -18016.15, -17882.19, -17801.83, -17625.08
   2 , ga.dtlz7.10.2 ,    -15994   ,  121 (               |         - *  ),-16147.93, -16074.36, -15994.50, -15967.08, -15888.58

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.3.singlePoint.dominanceCount.50.40.dtlz7.20.2 ,    -19151   ,  102 (       ------- | *  -------   ),-19273.25, -19191.29, -19151.85, -19121.40, -19036.49
   1 , ga.dtlz7.20.2 ,    -19153   ,  164 (     --------  | * ------     ),-19297.83, -19204.12, -19153.31, -19130.53, -19055.91

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz7.40.2 ,    -19189   ,  162 (   -----       *     -------  ),-19290.51, -19251.65, -19189.26, -19128.72, -19066.76
   1 , tunedga.0.3.TwoPoint.continuousDominanceLoss.50.40.dtlz7.40.2 ,    -19185   ,  151 (   --------    *     -------- ),-19291.84, -19220.31, -19185.40, -19129.43, -19054.87

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.3.TwoPoint.continuousDominanceLoss.50.80.dtlz7.10.4 ,    -37133   ,  284 ( -   *---      |              ),-37358.87, -37313.46, -37133.34, -37108.35, -36856.41
   2 , ga.dtlz7.10.4 ,    -35767   ,  309 (               |      -  *--- ),-35993.32, -35870.41, -35767.73, -35699.57, -35470.75

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz7.20.4 ,    -38408   ,  231 (    ------    *|    --        ),-38577.01, -38477.47, -38408.30, -38309.56, -38281.85
   1 , tunedga.0.1.singlePoint.dominanceCount.50.80.dtlz7.20.4 ,    -38363   ,  170 (     -----     | * ---        ),-38559.23, -38475.82, -38363.66, -38327.35, -38280.67

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.3.uniform.continuousDominanceLoss.50.40.dtlz7.40.4 ,    -38458   ,  304 ( -------    *  |  --------    ),-38687.55, -38549.79, -38458.34, -38327.48, -38175.34
   1 , ga.dtlz7.40.4 ,    -38425   ,  281 (--------      *|   ------     ),-38695.23, -38532.79, -38425.43, -38308.90, -38190.02

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.1.singlePoint.continuousDominanceLoss.50.40.dtlz7.10.6 ,    -56679   ,  360 (----  * --     |              ),-57109.57, -56809.50, -56679.67, -56557.85, -56414.57
   2 , ga.dtlz7.10.6 ,    -55609   ,  314 (               | --  *---     ),-55897.98, -55765.29, -55609.26, -55497.30, -55292.85

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz7.20.6 ,    -58171   ,  323 (              -|--- *     --- ),-58470.28, -58208.26, -58171.04, -57913.34, -57787.40
   1 , tunedga.0.1.uniform.dominanceRank.50.20.dtlz7.20.6 ,    -58123   ,  305 (               |---- *    --- ),-58403.35, -58195.26, -58123.04, -57944.37, -57789.16

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz7.40.6 ,    -58160   ,  366 (      ----- *  |------        ),-58402.79, -58226.30, -58160.40, -58054.13, -57821.68
   1 , tunedga.0.3.singlePoint.continuousDominanceLoss.50.40.dtlz7.40.6 ,    -58155   ,  383 (      ----   * |-------       ),-58394.93, -58245.83, -58155.35, -58033.65, -57803.37

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.3.TwoPoint.continuousDominanceLoss.50.20.dtlz7.10.8 ,    -76281   ,  258 (  ------   *---|              ),-76806.28, -76457.42, -76281.72, -76224.44, -76067.34
   2 , ga.dtlz7.10.8 ,    -75630   ,  289 (               |----  *  ---- ),-75980.74, -75766.52, -75630.53, -75493.55, -75248.95

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , ga.dtlz7.20.8 ,    -78089   ,  310 (    ---------- |*  -----      ),-78508.76, -78143.03, -78089.71, -77959.25, -77792.17
   1 , tunedga.0.3.singlePoint.dominanceRank.50.20.dtlz7.20.8 ,    -78075   ,  329 (      ---------|*  ------     ),-78445.92, -78130.22, -78075.06, -77969.02, -77755.13

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , tunedga.0.3.singlePoint.continuousDominanceLoss.50.80.dtlz7.40.8 ,    -77938   ,  398 (               |      --- *-- ),-78273.05, -77955.18, -77938.46, -77774.72, -77610.87
   1 , ga.dtlz7.40.8 ,    -77935   ,  466 (               |-------   *-  ),-78866.10, -78225.31, -77935.27, -77826.04, -77684.54
```

## Threats to Validity

The experiment is carried out with only one baseline populations, this results might be varying with another set of baseline populations.  We only used 3 varied options over the GA each default parameter. The DE used is terminated early by the early termination criteria.

## Future Work

* The default parameters used in the GAs are not tuned to the problems. The mutation rate, crossover and the size of populations  can be adjusted to improve the solutions on the paretofrontier.

* We used KrallsBstop method to impose early stopping criteria. We can use different defaults in the implementation. We can alternatively use another approach to determine early stopping criteria, probably cdomloss from first generation to the current generation. If the loss numbers are changing, increasing, we see improvement and push for few more genenrations. We can also use hypervolume over here.


## The Acknowledgments

We thank Dr. Menzies for the statistical machinery code for scottknott, bootstrap, a12, cohens e.t.c shared with us for the class homework projects.[6]

___References:___

1.  _Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Transactions on Evolutionary Computation, 6(2), 182–197. http://doi.org/10.1109/4235.996017_

2.  _Kautz, H., Selman, B., & Jiang, Y. (n.d.). A General Stochastic Approach to Solving Problems with Hard and Soft Constraints, 0, 1–14._

3. _Deb, K., Thiele, L., Laumanns, M., Zitzler, E., Abraham, A., Jain, L., & Goldberg, R. (2005). Scalable test problems for evolutionary multiobjective optimization. Evolutionary Multiobjective, (1990), 1–27. http://doi.org/10.1007/1-84628-137-7_

4. _Timm Menzies. https://github.com/txt/mase/blob/master/lessthan.md_

5. _Timm Menzies. https://github.com/txt/ase16/blob/master/doc/stats.md_

6. _Timm Menzies. https://github.com/txt/ase16/blob/master/src/stats.py_

7. _Timm Menzies. https://github.com/txt/ase16/blob/master/doc/nsga2spea2.md_

6. Andrea Arcuri and Lionel Briand. 2011. A practical guide for using statistical tests to assess randomized algorithms in software engineering. In Proceedings of the 33rd International Conference on Software Engineering (ICSE '11). ACM, New York, NY, USA, 1-10. DOI=http://dx.doi.org/10.1145/1985793.1985795


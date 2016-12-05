# Homework 8 - Implement NSGAII

___Not w ___

_keywords: optimization, random, searching_


## Introduction
Not all problems are easy to solve using simple deterministic algorithms. More often than not we have problems for which we make some decisions and end up with some quantitative results, which are our objectives, all as a consequence of our choices for those decisions. But the lingering question for anyone is how to manage their decisions so that they get gain margin over the set of objectives they care for. This spawns them with several more questions, on whether they can have good number of optimal solutions, useful in making practical decisions. Such optimal solutions are achieved by random searching or unordered searching. Ordered searching requires us to make tricky decisions when choosing next decision or set of decisions in the series of decisions we make, but unordered search does not assume any knowledge. It is rich with possibilities and might give good insights into the uncharted territory which is otherwise dark using the ordered search using deterministic algorithms.Random searching for solution rigorously seems a naive brute-force way to solve the problem, it takes no assumptions of the kind of problem and is also not guaranteed to provide a best solution. But more often than not these optimizing random search provides close to real solutions, by using some techniques in the way of searching. These random searches also known as stochastic searches, take advantage of the todays CPU speeds, and memory access speeds and other state of the art chip technologies used to built todays computing devices. 

Most of the algorithms that perform the unordered search do the mutation on the set of decisions to randomly traverse over the solution space. Mutation is a operation, which is changing the part of the solution, which as mentioned earlier contains set of decisions. Two identifiable trends can be understood when we look at the algorithms that perform unordered search, namely local search and stochastic search. Local search involves mutating a part of the solution such that we achieve optimal objectives with the this search. Stochastic search as the name says, is a straight forward - mutation and search paradigm, where we perform mutation, look the objective for this solution and keep searching.


Another set of algorithms came along that are inspired by the Genetic Algorithm, which fundamentally perform crosover and mutatio over a generation of populations. Then prune the less evloved individuals using a process called elitism. This process is called Generation , and we run this for more generation until we get a convergence on the generations. Also we no longer get a single best solution as we have multi-objectives. We look for a optimized frontier called Pareto Frontier, which is the frontier on which all objectives competing and non-competing settle for optimality.


## Background

GA inspired algorithms are optimizers for finding more than one solutions with multi-objectives began in the 1990s namely NSGA, NPGA, MOGA e.t.c . The diversity of the solutions or frontier is maintained by performing crowd pruning and elitism.

The elitism is decided some apporaches

* dominance Rank
* dominance Count
* dominance Depth

### NSGAII

NSGAII is a variant of GA and Uses the dominance depth in the elitism step. Additionally it uses cuboid sorting for futher pruning on individuals on same depth.

![nsga2](https://github.com/txt/ase16/blob/master/img/nsgaii.png)

NSGAII uses the concept of frontier partition based on the dominance depth, when it wants to make a further decision to prune individuals in the frontier that cuts off into the required size of the generation is performed by cuboid sorting.

![cuboid sorting](https://github.com/txt/ase16/blob/master/img/cuboid.png)


### Continuous Dominance Loss

As mentioned earlier we type 3 comaparision for evaluating the performance of the optimizers. Contiuous Dominance is another parameter bsaed on the continuous dominance value alculated between two individuals. For each individual in first generation we add the loss he makes on all the individuals in the final generation, then we add all the losses made by all te individuals in the first generation.

## Evaluation

GA is coded up and extended with nondominated sort and cuboid sorting in the elitism step. Another variant is coded up which uses CdomLoss and dominance count for the elitism step. 


These algorithms are run over DTLZ line of problems namely DTLZ with 2,4,6,8 with 10,20,40 which is total of 12 problems and run on the above two optimizers.

Same 20 baseline populations are used for a problem to run against the variants of the optimizers.

Cdomloss is calculated between the first generation and the final generation. Since we have 20 baseline populations we get 20 numbers. These performance numbers are then feed to scottknott for statistical analysis. 


## Results and Discussion

We got the following scottknott results by running the problems with the two variants of the GA. For each problem we ranked the resuts with gacdom loss variant and the nsga2 variant. We find that MORE OFTEN THAN NOT GACDOMLOSS variant is performing better or equal than the NSGAII variant for the problems. 


```bash
rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.10.2.gacdom ,    -39790   ,   73 (--  *  -       |              ),-39856.16, -39823.79, -39790.14, -39753.17, -39726.40
   2 , dtlz1.10.2.nsga2 ,    -39706   ,  138 (    ---   *   -|              ),-39799.06, -39749.32, -39706.51, -39646.11, -39599.68

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.10.4.gacdom ,    -79620   ,  137 (-----  *  --   |              ),-79747.33, -79650.19, -79620.87, -79562.37, -79528.81
   2 , dtlz1.10.4.nsga2 ,    -79351   ,  184 (            ---|     * ----   ),-79528.38, -79438.44, -79351.98, -79307.11, -79240.06

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.10.6.gacdom ,    -118822   ,  195 (   --  *  -----|              ),-118979.56, -118896.62, -118822.60, -118728.06, -118551.07
   2 , dtlz1.10.6.nsga2 ,    -118539   ,  267 (        -----  *   -------    ),-118775.71, -118610.39, -118539.48, -118406.18, -118136.47

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.10.8.gacdom ,    -156102   ,  467 ( -  *  -----   |              ),-156350.86, -156287.47, -156102.51, -155839.68, -155428.18
   2 , dtlz1.10.8.nsga2 ,    -154339   ,  449 (               |    --   * -  ),-154733.30, -154577.87, -154339.69, -154164.54, -154050.43

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.20.2.gacdom ,    -39957   ,   54 (-- *   --------|-             ),-39981.45, -39965.53, -39957.95, -39934.42, -39857.44
   1 , dtlz1.20.2.nsga2 ,    -39953   ,   33 (--- * ---------|-             ),-39982.12, -39964.64, -39953.87, -39936.47, -39859.76

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.20.4.gacdom ,    -79956   ,   55 (- *----        |              ),-79983.08, -79969.24, -79956.66, -79934.25, -79879.86
   1 , dtlz1.20.4.nsga2 ,    -79950   ,   29 ( -*-------     |              ),-79968.62, -79960.16, -79950.04, -79934.68, -79841.54

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.20.6.gacdom ,    -119940   ,   53 (- * --         |              ),-119972.30, -119963.87, -119940.31, -119918.22, -119880.30
   2 , dtlz1.20.6.nsga2 ,    -119760   ,  149 (    ---       *|----          ),-119914.51, -119862.35, -119760.65, -119736.64, -119663.25

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.20.8.gacdom ,    -159952   ,   25 (*-             |              ),-159969.10, -159957.55, -159952.47, -159942.03, -159873.75
   2 , dtlz1.20.8.nsga2 ,    -159719   ,  163 (    -  *-------|------        ),-159831.23, -159798.16, -159719.48, -159662.32, -159198.73

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.40.2.gacdom ,    -39991   ,   23 ( * ------------|-------       ),-39997.75, -39997.04, -39991.99, -39979.00, -39855.68
   1 , dtlz1.40.2.nsga2 ,    -39965   ,   69 (-    *    -----|------------- ),-39996.18, -39989.11, -39965.88, -39936.69, -39819.28

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.40.4.gacdom ,    -79991   ,   36 ( *------       |              ),-79998.73, -79996.58, -79991.00, -79983.94, -79947.58
   1 , dtlz1.40.4.nsga2 ,    -79990   ,   24 ( *  ------     |              ),-79998.76, -79996.40, -79990.72, -79973.55, -79933.81

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.40.6.gacdom ,    -119992   ,   14 (*--------      |              ),-119999.05, -119998.34, -119992.85, -119986.80, -119873.51
   1 , dtlz1.40.6.nsga2 ,    -119979   ,   98 ( * ----------- |              ),-119996.09, -119991.18, -119979.33, -119949.58, -119813.94

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz1.40.8.gacdom ,    -159995   ,    9 (*-             |              ),-159999.15, -159998.17, -159995.20, -159989.58, -159965.95
   1 , dtlz1.40.8.nsga2 ,    -159993   ,   11 (*--            |              ),-159998.47, -159996.94, -159993.32, -159989.87, -159948.61

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.10.2.gacdom ,    -39382   ,  235 ( --   * ---    |              ),-39545.50, -39467.42, -39382.36, -39305.33, -39199.96
   2 , dtlz3.10.2.nsga2 ,    -38972   ,  278 (        ----   | * -----      ),-39300.96, -39152.32, -38972.92, -38916.87, -38739.76

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.10.4.gacdom ,    -78867   ,  355 (   --        * |   ----       ),-79106.22, -79056.00, -78867.07, -78728.85, -78627.89
   1 , dtlz3.10.4.nsga2 ,    -78893   ,  353 (    ---     *  |  ----------- ),-79079.19, -79015.13, -78893.93, -78754.42, -78478.39

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.10.6.gacdom ,    -117872   ,  429 (         ---   |*  ------     ),-118242.11, -118038.47, -117872.46, -117707.24, -117380.60
   1 , dtlz3.10.6.nsga2 ,    -117776   ,  466 (           ----| *   -------- ),-118098.56, -117903.61, -117776.47, -117582.16, -117119.85

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.10.8.gacdom ,    -158515   ,  327 ( --- *  -----  |              ),-158762.67, -158600.22, -158515.79, -158344.24, -158065.62
   2 , dtlz3.10.8.nsga2 ,    -157679   ,  504 (            ---|-   * -----   ),-158104.87, -157857.59, -157679.68, -157548.89, -157257.87

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.20.2.gacdom ,    -39939   ,   47 (  --    *  ----|--            ),-39969.75, -39956.39, -39939.16, -39920.67, -39883.31
   1 , dtlz3.20.2.nsga2 ,    -39932   ,   51 (   ----- *     |---------     ),-39962.40, -39939.69, -39932.13, -39897.37, -39846.30

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.20.4.gacdom ,    -79809   ,  130 (---   *   -----|-------       ),-79894.86, -79854.40, -79809.86, -79747.43, -79566.80
   1 , dtlz3.20.4.nsga2 ,    -79790   ,   87 (     --*  -----|----          ),-79823.71, -79803.00, -79790.37, -79749.16, -79611.77

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.20.6.nsga2 ,    -119932   ,   34 ( *--           |              ),-119958.19, -119948.22, -119932.78, -119917.44, -119875.26
   1 , dtlz3.20.6.gacdom ,    -119933   ,   36 (-*--           |              ),-119961.60, -119941.72, -119933.50, -119912.14, -119868.65

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.20.8.gacdom ,    -159675   ,  134 (--  * --       |              ),-159780.21, -159726.96, -159675.78, -159613.72, -159554.54
   2 , dtlz3.20.8.nsga2 ,    -159419   ,  224 (      ---   *  |-------       ),-159604.79, -159531.83, -159419.20, -159341.41, -159112.88

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.40.2.gacdom ,    -39994   ,   18 (*--------------|              ),-39998.09, -39996.34, -39994.15, -39988.50, -39909.78
   1 , dtlz3.40.2.nsga2 ,    -39992   ,   14 ( *------------ |              ),-39998.02, -39996.25, -39992.57, -39986.07, -39916.30

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.40.4.gacdom ,    -79997   ,    3 (*              |              ),-79999.20, -79998.35, -79997.26, -79995.91, -79988.74
   2 , dtlz3.40.4.nsga2 ,    -79968   ,   60 ( -*  ----------|-             ),-79983.36, -79974.19, -79968.14, -79929.57, -79770.49

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.40.6.gacdom ,    -119983   ,   16 ( *-            |              ),-119997.33, -119987.97, -119983.80, -119975.38, -119957.09
   2 , dtlz3.40.6.nsga2 ,    -119946   ,   65 ( -- *   -----  |              ),-119978.42, -119956.92, -119946.20, -119903.24, -119852.78

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz3.40.8.gacdom ,    -159996   ,    7 (*              |              ),-159999.43, -159998.42, -159996.88, -159992.15, -159964.61
   2 , dtlz3.40.8.nsga2 ,    -159913   ,  155 (  *   ---      |              ),-159979.18, -159972.09, -159913.19, -159817.35, -159720.86

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.10.2.gacdom ,    -39800   ,    0 (*              |              ),-39800.00, -39800.00, -39800.00, -39800.00, -39800.00
   1 , dtlz5.10.2.nsga2 ,    -39800   ,    0 (*              |              ),-39800.00, -39800.00, -39800.00, -39800.00, -39800.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.10.4.gacdom ,    -79600   ,    0 (*              |              ),-79600.00, -79600.00, -79600.00, -79600.00, -79600.00
   1 , dtlz5.10.4.nsga2 ,    -79600   ,    0 (*              |              ),-79600.00, -79600.00, -79600.00, -79600.00, -79600.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.10.6.gacdom ,    -119400   ,    0 (*              |              ),-119400.00, -119400.00, -119400.00, -119400.00, -119400.00
   1 , dtlz5.10.6.nsga2 ,    -119400   ,    0 (*              |              ),-119400.00, -119400.00, -119400.00, -119400.00, -119400.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.10.8.gacdom ,    -155464   ,  220 (  ---* ---     |              ),-155681.10, -155496.02, -155464.90, -155327.96, -155133.26
   2 , dtlz5.10.8.nsga2 ,    -154699   ,  394 (               |*  --------   ),-154867.75, -154826.75, -154699.82, -154533.23, -153947.49

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.20.2.gacdom ,    -39800   ,    0 (*              |              ),-39800.00, -39800.00, -39800.00, -39800.00, -39800.00
   1 , dtlz5.20.2.nsga2 ,    -39800   ,    0 (*              |              ),-39800.00, -39800.00, -39800.00, -39800.00, -39800.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.20.4.gacdom ,    -79600   ,    0 (*              |              ),-79600.00, -79600.00, -79600.00, -79600.00, -79600.00
   1 , dtlz5.20.4.nsga2 ,    -79600   ,    0 (*              |              ),-79600.00, -79600.00, -79600.00, -79600.00, -79600.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.20.6.gacdom ,    -119400   ,    0 (*              |              ),-119400.00, -119400.00, -119400.00, -119400.00, -119400.00
   1 , dtlz5.20.6.nsga2 ,    -119400   ,    0 (*              |              ),-119400.00, -119400.00, -119400.00, -119400.00, -119400.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.20.8.gacdom ,    -159200   ,    0 (*              |              ),-159200.00, -159200.00, -159200.00, -159200.00, -159200.00
   1 , dtlz5.20.8.nsga2 ,    -159200   ,    0 (*              |              ),-159200.00, -159200.00, -159200.00, -159200.00, -159200.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.40.2.gacdom ,    -39800   ,    0 (*              |              ),-39800.00, -39800.00, -39800.00, -39800.00, -39800.00
   1 , dtlz5.40.2.nsga2 ,    -39800   ,    0 (*              |              ),-39800.00, -39800.00, -39800.00, -39800.00, -39800.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.40.4.gacdom ,    -79600   ,    0 (*              |              ),-79600.00, -79600.00, -79600.00, -79600.00, -79600.00
   1 , dtlz5.40.4.nsga2 ,    -79600   ,    0 (*              |              ),-79600.00, -79600.00, -79600.00, -79600.00, -79600.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.40.6.gacdom ,    -119400   ,    0 (*              |              ),-119400.00, -119400.00, -119400.00, -119400.00, -119400.00
   1 , dtlz5.40.6.nsga2 ,    -119400   ,    0 (*              |              ),-119400.00, -119400.00, -119400.00, -119400.00, -119400.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz5.40.8.gacdom ,    -159200   ,    0 (*              |              ),-159200.00, -159200.00, -159200.00, -159200.00, -159200.00
   1 , dtlz5.40.8.nsga2 ,    -159200   ,    0 (*              |              ),-159200.00, -159200.00, -159200.00, -159200.00, -159200.00

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.10.2.nsga2 ,    -35789   ,  731 (  --- * -      |              ),-36537.47, -36006.22, -35789.72, -35435.02, -35216.13
   2 , dtlz7.10.2.gacdom ,    -31804   ,  453 (               |           *- ),-32053.87, -31964.39, -31804.51, -31667.49, -31476.95

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.10.4.nsga2 ,    -77799   , 1114 (-- * --        |              ),-78634.96, -78293.71, -77799.40, -77438.72, -76733.68
   2 , dtlz7.10.4.gacdom ,    -71320   ,  458 (               |          *-  ),-71725.34, -71577.64, -71320.57, -71133.01, -70716.89

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.10.6.nsga2 ,    -118395   ,  931 (  -- *-        |              ),-119509.23, -118813.58, -118395.29, -118036.94, -117689.40
   2 , dtlz7.10.6.gacdom ,    -110965   ,  749 (               |         - *- ),-111689.48, -111330.35, -110965.69, -110754.41, -110377.53

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.10.8.nsga2 ,    -156919   , 2382 (  ----------  *|---           ),-162283.28, -157849.67, -156919.00, -156610.71, -154819.02
   2 , dtlz7.10.8.gacdom ,    -150631   ,  380 (               |             *),-151004.32, -150757.43, -150631.48, -150477.07, -150293.67

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.20.2.nsga2 ,    -39490   ,  222 ( --* ---       |              ),-39696.07, -39546.02, -39490.55, -39377.34, -39118.23
   2 , dtlz7.20.2.gacdom ,    -37378   ,  144 (               |          -*- ),-37490.42, -37437.74, -37378.52, -37352.55, -37205.18

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.20.4.nsga2 ,    -78878   ,  485 (    --*-       |              ),-79429.12, -78974.11, -78878.83, -78650.89, -78529.96
   2 , dtlz7.20.4.gacdom ,    -74535   ,  550 (               |         -* - ),-74789.97, -74677.29, -74535.04, -74192.93, -74015.15

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.20.6.nsga2 ,    -118679   ,  635 (  - *-         |              ),-119095.83, -118905.33, -118679.13, -118449.66, -118098.54
   2 , dtlz7.20.6.gacdom ,    -112923   ,  407 (               |         - *- ),-113455.33, -113116.65, -112923.07, -112802.62, -112366.25

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.20.8.nsga2 ,    -158521   ,  766 (   -* --       |              ),-158808.61, -158603.94, -158521.92, -157975.07, -157491.65
   2 , dtlz7.20.8.gacdom ,    -152215   ,  537 (               |       --- *- ),-153181.79, -152480.58, -152215.46, -151998.47, -151477.93

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.40.2.nsga2 ,    -39491   ,  229 (   - *---      |              ),-39702.66, -39583.15, -39491.49, -39446.01, -39126.64
   2 , dtlz7.40.2.gacdom ,    -37444   ,  193 (               |       --- *- ),-37857.20, -37530.87, -37444.04, -37394.98, -37276.06

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.40.4.nsga2 ,    -78854   ,  375 (  - *-         |              ),-79220.24, -78969.66, -78854.54, -78629.82, -78436.69
   2 , dtlz7.40.4.gacdom ,    -74340   ,  427 (               |        - *-  ),-74590.59, -74511.49, -74340.31, -74145.03, -73849.36

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.40.6.nsga2 ,    -118374   ,  491 ( --*-          |              ),-118957.86, -118564.10, -118374.96, -118148.41, -117958.26
   2 , dtlz7.40.6.gacdom ,    -113013   ,  355 (               |        --*-- ),-113443.32, -113127.77, -113013.24, -112898.44, -112366.65

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 , dtlz7.40.8.nsga2 ,    -158117   ,  596 (   -- *-       |              ),-158908.14, -158428.33, -158117.17, -157976.81, -157494.70
   2 , dtlz7.40.8.gacdom ,    -152410   ,  323 (               |        - *   ),-152954.20, -152476.93, -152410.79, -152270.76, -152043.94

```


## Threats to Validity

The solutions obtained in the final pareto frontier may be  more improvised by using tuned defaults for the underlying GA. We can the mutation rate, which can give us better solutions and converge sooner, with less duplicates or more diversity on solutions.

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


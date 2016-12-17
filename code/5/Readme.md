# Homework 5

## MaxWalkSat

Code : [Osyczka2.py](https://github.com/tnkteja/fss16ntadiko/blob/hw5/code/5/Osyczka2.py)

Results:

![Osyczka.png](https://rawgit.com/tnkteja/fss16ntadiko/hw5/code/5/.images/Osyczka.png)

## Review 4

###  Theory

1. State few drawbacks of stochastic optimizers.

   Answer :  The main drawback is they are not deterministic algorithms and they don't guarantee a solution, it is hard to find if a solution exists, unlike for a deterministic algorithm we can find if a solution exists. Other drawbacks ar

2. What is pareto optimality? Describe using a graphical example.

1. What is the problem with local maxima?

1. In the following diagram, each square has the same x,y,z axis. What might the names of those x,y,z values?
![](https://github.com/timm/sbse14/wiki/etc/img/landscape/WrightFitness.jpg)

2. Explain the following, using the above diagram:

 * Holes
 * Poles
 * Saddles
 * Local minima
 * Flat
 * Brittle

3. Explain the following term and describe how it handles the problem of flat: Retries.

4. How does the following techniques avoid the problems of local maxima?

  Simulated annealing
    - Retries
    - Momentum (make sure you explain momentum)
  
5. Local search can be characterized as follows

   + Jump all around the hills
   + Sometimes, sitting still while rolling marbles left and right
   + Then taking one step along the direction where the marbles roll the furthest.
   + Go to 1.

In the following code snippet, explain where you'd find 5.
```
FOR i = 1 to max-tries DO
  solution = random assignment
  FOR j =1 to max-changes DO
    IF  score(solution) > threshold
        THEN  RETURN solution
    FI
    c = random part of solution 
    IF    p < random()
    THEN  change a random setting in c
    ELSE  change setting in c that maximizes score(solution) 
    FI
RETURN failure, best solution found
```


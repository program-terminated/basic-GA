# Mutation

Mutation is more exploitative as it makes only minor changes to an individual.
Since mutation introduces completely new genetic information, it is effective at preventing the GA from getting stuck at local optima.

The mutation methods that I have implemented are **insertion mutation**, **scramble mutation**, and **inversion mutation**. 
Due to the number of different mutation implementations, we are able to change our implementation during a run. 
That is, we can start with a more disruptive mutation method and, as the run progresses, switch to a less disruptive one.

## Insert mutation 

Insert mutation randomly picks 2 alleles (genes) and moves them to be next to each other, shifting the rest of the individual to compensate.

## Scramble mutation 

Scramble mutation randomly selects a subset of an individual and randomly scrambles it. The subset does not need to be contiguous, but I usually implement it as a 
contiguous subset. The length of the subset is a hyperparameter.

## Inversion mutation 

Inversion mutation randomly selects 2 alleles and inverts the substring between them. 
This is a very specialized mutation function specifically designed for Travelling Salesperson-esque problems.
That is, it is designed for problems where an optimized route needs to be found. 
Although this is it's indended purpose, it can still be used in other problem instances.

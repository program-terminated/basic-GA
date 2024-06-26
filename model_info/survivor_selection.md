# Survivor Selection

The main consideration with survivor selection is if, for each generation, we consider the current generation as well as offspring or just the offspring. 
The two basic *fitness-bassed selections* are **(μ + λ) selection** and **replacement**, where there are *μ* parents and *λ* offspring.

I have implemented survivor selection with *fitness-based selection*. I will briefly mention that there is also an age-based implementation, 
a fitness-based **round-robin** implementation, **(μ, λ)** implementation, and the option to include **elitism**.

## (μ + λ) selection

In *(μ + λ)* ("mu plus lambda") there is greater selection pressure (due to the higher number of individuals that could survive) and is thus better for 
exploitation. In *(μ + λ)*, we combine the entire current generation and offspring, rank them based on fitness, and take the *μ* fittest.

## Replacement

In replacement, we often have *μ > λ*, meaning we have more current generation members than offspring and that some members of the current population are 
guaranteed to survive. We then sort the current generation by fitness and replace the *λ* lowest fitness individuals with the offspring.

## Other selection methods

### Age-based selection

In age-based survivor selection, fitness is not considered. The GA keeps track of how many generations each individual has been in the population and 
removes it once a specified threshold has been exceeded.

### Round-robin selection

In fitness-based round-robin survivor selection, each individual is put against *q* other individuals and whichever individual has the higher fitness wins. 
The *μ* individuals with the most wins are selected for the next generation. Common practice is *q* = 10. As *q* increases, it becomes increasingly unlikely 
that less fit individuals will be selected until it becomes deterministic.

### (μ, λ) selection

Perhaps the most aggressive form of survivor selection mentioned here, *(μ, λ)* is associated with Evolutionary Strategies (ES), which are strategies 
for the functions in genetic algorithms. In this case, *μ* is the number of parents and *λ* is the number of offspring. In *(μ, λ)*, we take the *λ* offspring 
based on their fitness and pick the *μ* fittest to be the next generation. The aggresiveness of this implementation comes from the fact that there are 
vastly more offspring than parents, often *λ = 7μ*.

## Elitism

Elitism is when we make exact copies of some of the fittest individuals from the current generation into the next generation to ensure they are not lost. 
This is typically done in non-deterministic survivor selection implementations.

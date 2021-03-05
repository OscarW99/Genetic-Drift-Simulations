# Genetic-Drift-Simulations
Genetic drift is the change in the frequency of an allele in a population over multiple generations. An individual’s alleles are a sample of those in present their parents and chance has a role in determining whether that individual will survive and reproduce. Genetic drift may cause gene variants to disappear completely from a population and thereby reduce genetic variation. This code simulates two simple genetic drift models. 


required packages: **matplotlib**, **random**


# **Simulation 1**

Start with population of 100, half of which have allele ‘A’ and half which have allele ‘B’.
computes 1000 generations where with each generation an allele from the current population is randomly selected and added to a new population.
The random selection occurs the same number of times as the population size (100) so that the new and original populations are the same size.

If either of the alleles is completely lost from the population then no further generations are completed.

Produces a plot that shows the change in allele frequency with each generation, up to the 1000 generations or when either allele is lost.



# **Simulation 2**

Start with population of 100.
This time there are 2 alleles for a gene ‘A’ present in each individual. The
alleles are ‘A’ and ‘a’ and the individuals are either ‘AA’, ‘Aa’ or ‘aa’.

The initial population has an even distribution of alleles so 25% are “AA”, 50% “Aa” (25%
‘Aa’ and 25% ‘aA’) and 25% “aa”.

An evolutionary event has occurred that means only 80% of ‘aa’ individuals will survive to
maturity to breed.
The population size remains static at 100 after each generation.
With each generation one allele from each random individual is combined with one allele from another random individual to create a new population of 100. As ‘aa’ is only 80% successful it means that the new population only includes 80% of those created (so 1 in 5 of the 'aa's created are rejected and a new individual is created in its place).

Computes 500 generations or until allele “a” disappears from the population.
Draws a plot of ‘AA’, ‘Aa’, and ‘aa’. 

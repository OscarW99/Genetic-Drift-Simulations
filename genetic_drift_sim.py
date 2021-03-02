# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:31:51 2020

@author: oscar
"""



import random
import matplotlib.pyplot as plt


############################################## FUNCTIONS #################################################
##########################################################################################################

# A function that takes a dictionary of alleles and their associated probabilities and for a stated
# population size returns a list that represents allele distribution for that population size.
# Example inputs: ({'A':0.5, 'B':0.5}, 100)        Example output: ['A', 'A', 'A' ,...,'B','B','B']

def createPopulation(allele_dictionary, population_size = 100):
    
    population_array = [] # initiate population list
    
    allele_list = allele_dictionary.keys() # create list of alleles from dictionary parameter
    for allele in allele_list:
        number_of_individuals = int(allele_dictionary[allele]*population_size)
        for i in range(number_of_individuals):
            population_array.append(allele)

    return population_array


##########################################################################################################
    
# A function that takes a population list containing 2 alleles and a generation number and returns a 3D array 
# that contains populations for each generation for as many generations as specified 
# or for as many generations as it takes for an allele to be fully removed
# Example input: ['A', 'A', 'A' ,...,'B','B','B']   example output: [....['A', 'A' ,...,'A','B'], ['A', 'A',..., 'A', 'A']]

def computeGenerations1(population_array, number_of_generations = 1000):
    
    all_generations = [] # used to hold all population lists after each iteration and will be returned at the end
    pop = population_array
    all_generations.append(pop) # start by adding the initial population
    
    for i in range(number_of_generations): #compute a specified number of generations
        next_gen = [] # initiate list to hold the new generation
        for i in range(len(population_array)): # make new population the same size as the previous
            individual = random.choice(pop)  
            next_gen.append(individual) # randomly select alleles from the previous population and add to 'next_gen'
            
        all_generations.append(next_gen) # add the newly formed generation 'next_gen' to the 'all_generations' list which holds populations for all generations.
        
        alleles = list(set(population_array))  # If either of the alleles have been fully removed, break out of the loop
        if alleles[0] not in next_gen or alleles[1] not in next_gen:
            break 
        
        pop = next_gen # change the pop varibale to the latest generation before restarting the loop
    
    return all_generations # Returns a 3D array of populations at each generation.


##########################################################################################################   

# A function that takes a poplation list for 3 allele pairs and a generation number and returns a 3D array
# containing populations for each generation for as many generations as specified or until an allele is removed
# Includes optional parameter for allele fitness
# Example input: (['AA',.., 'Aa',.., 'Aa',.., 'aa'], aa = 0.8)   example output: [...['AA', 'AA' ,..,'AA','Aa'], ['AA', 'AA',...., 'AA', 'AA']]
    
def computeGenerations2(population_array, number_of_generations = 500, **fitness):
    
    all_generations = [] # To be returned
    pop = population_array
    all_generations.append(pop) # add intital population 
    
    for i in range(number_of_generations): # compute specified generations
        next_gen = [] # initiate new population
        for i in range(len(population_array)):
            for i in range(2): # take a random allele from 2 random individulas in the population and add them to 'next_gen' list
                individual = random.choice(pop)
                allele = random.choice(individual) 
                next_gen.append(allele) 
                
        # next_gen now has 200 individual alleles so need to pair them up.
        next_gen = [next_gen[i] + next_gen[i+1] for i in range(0, len(next_gen), 2)] 
       
        # This code block is only run if fitness paramter is added
        for key in fitness.keys(): 
            early_death = int(next_gen.count(str(key)) * ((1-fitness[key])) + 0.00001) # This variable represents the number of allele pairs
            # to remove. We want to round down as we can't have a fraction of an allele. The +0.00001 accounts for floating point errors
            for i in range(int(early_death)):
                next_gen.remove(key) # remove allele from population list
                pair = ""
                individual1 = random.choice(pop)
                allele1 = random.choice(individual1) 
                individual2 = random.choice(pop) 
                allele2 = random.choice(individual2)
                pair += allele1 + allele2
                next_gen.append(pair) # add back in another allele pair by combining random alleles from the parent population

        next_gen = [item.replace('aA', 'Aa') for item in next_gen] # This will make frequency calculations easier 

        all_generations.append(next_gen) #after new population is formed and adjusted for allele fitness, add this generation
        # to 'all_generations' that holds the population for each generation.
        
        if len(list(set(next_gen))) == 1:
            break  # if only one allele pair remians then break out of loop
        
        pop = next_gen # change the pop varibale to the latest generation before restarting the loop
    
    return all_generations #this returns a list of all populations lists for each generation.


##########################################################################################################

# A function that will calculate allele frequency for a given allele in each population-list in a 3D array
# and will return a list of frequencies
# Example input: ('A',[[gen1],[gen2],[gen3],....])  example output: [0.5, 0.48, 0.46,...]
    
def alleleFreq(allele, generations_array):
    
    total_allele_freq = [] # initiate list to be returned
    
    for population in generations_array:
        allele_freq = population.count(allele)/len(generations_array[0]) #calculate allele frequency
        total_allele_freq.append(allele_freq) # add to initial list
        
    return total_allele_freq
    

##########################################################################################################
    
# A function that given a dictionary of alleles as keys and their frequency-lists as values, will plot them.  
# example input: {'A': [0.5, 0.48, 0.46,...], 'B': [0.5, 0.52, 0.54,...]}
    
def createPlot(allele_frequencies):
    
    # matplotlib.pyplot --- plotting all allele frequencies and labelling axis...
     for key, value in allele_frequencies.items():
         y_generations = [i for i in range(len(value))] # create yaxis (time) from the length of frequency lists which represents the number of generations
         plt.plot(y_generations, value, label = key)
    
     plt.xlabel('Time[generations]')
     plt.ylabel('Allele frequency')
     plt.title('Genetic Drift')
     plt.legend()
     plt.show()
    

##########################################################################################################

# A function to combine all functions required to run simulation 1. Allows it to be called easily.
     
def simulation1():
    
    allele_dict = {'A':0.5, 'B':0.5} # set alleles and their fitness in dictionary
    
    population = createPopulation(allele_dict) # call createPopulation function. Default population size = 100
    
    generations_array = computeGenerations1(population) # call computeGenerations function. Default #generations = 1000

    allele_frequencies = {} # create dictionary for alleles and their frequency lists
    for allele in allele_dict.keys():
        freq_list = alleleFreq(allele, generations_array)
        allele_frequencies[allele] = freq_list
        
    createPlot(allele_frequencies) # using the allele_frequencies dictionary, call the createPlot function

        
##########################################################################################################

# A function to combine all functions required to run simulation 2. Allows it to be called easily. 
    
def simulation2():
    
    allele_dict = {'AA':0.25, 'Aa':0.5, 'aa':0.25} # set alleles and their fitness in dictionary
    
    population = createPopulation(allele_dict) # call createPopulation function. Default population size = 100
    
    generations_array = computeGenerations2(population, aa = 0.8) # call computeGenerations function with fitness parameter added. Default #generations = 500

    allele_frequencies = {} # create dictionary for alleles and their frequency lists
    for allele in allele_dict.keys():
        freq_list = alleleFreq(allele, generations_array)
        allele_frequencies[allele] = freq_list
    
    createPlot(allele_frequencies) # using the allele_frequencies dictionary, call the createPlot function
  

##########################################################################################################   
##########################################################################################################   




simulation1()
simulation2()

    











"""
BRR
it's hot
Runs the breadthfirst4 script a number of times with different genomes

Leander
"""

from breadthfirst4 import main as bestfirst
from random import shuffle
import numpy

# Settings to run best first algorithm with
functionseq = 1
functionmut = 2
padding = True
stop = 10
genelength = 25
printer = True
plotter = False
genome = []
for gene in range(1, genelength+1):
    genome.append(gene)

nruns = 100

# The output variables
mutsums = []
mutsums2 = []
levels = []
times = []
costs = []

# Performing the runs with randomized genomes of requested length
for i in range(0, nruns):
    shuffle(genome)
    print("\nRun {}: genome to sequence: {}".format(i, genome))

    # Call bestfirst algorithm
    mutsum, mutsum2, level, cost, time = bestfirst(genome, functionseq, functionmut, padding, stop, printer, plotter)

    # Saving output
    mutsums.append(mutsum)
    mutsums2.append(mutsum2)
    levels.append(level)
    times.append(time)
    costs.append(cost)

# Printing results
print("\n\nAveraged results: ")
print("average mutsum:  {}".format(numpy.mean(mutsums)))
print("average mutsum2: {}".format(numpy.mean(mutsums2)))
print("average levels:  {} deep".format(numpy.mean(levels)))
print("average start cost:{}".format(numpy.mean(costs)))
print("average runtime: {} sec".format(numpy.mean(times)))


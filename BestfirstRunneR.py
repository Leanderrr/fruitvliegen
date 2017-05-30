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
functionmut = 3
padding = True
stop = 10
genelength = 25
printer = False
plotter = False
genome = []
for gene in range(1, genelength+1):
    genome.append(gene)

nruns = 100

# The output variables
mutsums = []
mutsums2 = []
levels = []
costs = []
mutationTracks1 = []
mutationTracks2 = []
sames = []
solutionNs = []
times = []

# Performing the runs with randomized genomes of requested length
for i in range(0, nruns):
    shuffle(genome)
    print("\nRun {}: genome to sequence: {}".format(i, genome))

    # Call bestfirst algorithm
    mutsum, mutsum2, level, cost, mutationTrack1, mutationTrack2, same, solutionN, time = bestfirst(genome, functionseq, functionmut, padding, stop, printer, plotter)

    # Saving output
    mutsums.append(mutsum)
    mutsums2.append(mutsum2)
    levels.append(level)
    costs.append(cost)
    mutationTracks1.append(mutationTrack1)
    mutationTracks2.append(mutationTrack2)
    sames.append(same)
    solutionNs.append(solutionN)
    times.append(time)

# Printing results
for i in range(0, nruns):
    print("mutationtracker1: {}".format(mutationTrack1))
    print("\nresults run {}: ".format(i))
    print("minimum  mutsum:  {}".format(mutsums[i]))
    print("minimum  mutsum2: {}".format(mutsums2[i]))
    print("outcome with min mutsum is same outcome as min mutsum2 {}".format(sames[i]))
    print("minimum levels:  {} deep".format(levels[i]))
    print("minimum level found on average in solution: {}".format(solutionNs[i]))
    print("start cost:{}".format(costs[i]))
    print("runtime: {} sec".format(times[i]))



sameFrac = sum(sames) / nruns
print("\n\nAveraged results: ")
print("average minimum  mutsum:  {}".format(numpy.mean(mutsums)))
print("average minimum  mutsum2: {}".format(numpy.mean(mutsums2)))
print("portion of times outcome with min mutsum is same outcome as min mutsum2 {}".format(sameFrac))
print("average minimum levels:  {} deep".format(numpy.mean(levels)))
print("minimum level found on average in solution nr: {}".format(numpy.mean(solutionNs)+1))
print("average start cost:{}".format(numpy.mean(costs)))
print("average runtime: {} sec".format(numpy.mean(times)))


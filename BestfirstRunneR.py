"""
BRR
it's hot
Runs the breadthfirst4 script a number of times with different genomes

Leander
"""

from bestfirstsearch import main as bestfirst
from flipsorter import main as flipsort
from random import shuffle
import numpy

# Settings to run best first algorithm with
functionseq = 1
functionmut = 3
padding = True
stop = 1
genelength = 25
printer = False
plotter = False
genome = []
for gene in range(1, genelength+1):
    genome.append(gene)

nruns = 100

# The output variables
genes = []
mutsums = []
mutsums2 = []
levels = []
fliplevels = []
flipmutsums = []
flipmutsums2 = []
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
    genes.append(genome)
    # Call bestfirst algorithm
    mutsum, mutsum2, level, cost, mutationTrack1, mutationTrack2, same, solutionN, time = bestfirst(genome, functionseq, functionmut, padding, stop, printer, plotter)

    fliplevel, flipmutsum, flipmutsum2 = flipsort(genome, plotter, printer)

    # Saving output
    mutsums.append(mutsum)
    mutsums2.append(mutsum2)
    levels.append(level)
    costs.append(cost)
    flipmutsums.append(flipmutsum)
    flipmutsums2.append(flipmutsum2)
    mutationTracks1.append(mutationTrack1)
    mutationTracks2.append(mutationTrack2)
    sames.append(same)
    solutionNs.append(solutionN)
    times.append(time)
    fliplevels.append(fliplevel)

# Printing results
print("\n\ngenomes = {};".format(genes))
print("mutationtracker1 = {};".format(mutationTracks1))
print("mutationtracker2 = {};".format(mutationTracks2))
print("mutsums = {};".format(mutsums))
print("mutsums2 = {};".format(mutsums2))
print("sames = {};".format(sames))
print("levels = {};".format(levels))
print("fliplevels = {};".format(fliplevels))
print("flipmutsum = {};".format(flipmutsums))
print("flipmutsum2 = {};".format(flipmutsums2))
print("solat = {};".format(solutionNs))
print("costs = {};".format(costs))
print("runtimes = {};".format(times))



sameFrac = sum(sames) / nruns
print("\n\nAveraged results: ")
print("average minimum  mutsum:  {}".format(numpy.mean(mutsums)))
print("average minimum  mutsum2: {}".format(numpy.mean(mutsums2)))
print("portion of times outcome with min mutsum is same outcome as min mutsum2 {}".format(sameFrac))
print("average minimum levels:  {} deep".format(numpy.mean(levels)))
print("minimum level found on average in solution nr: {}".format(numpy.mean(solutionNs)+1))
print("average start cost:{}".format(numpy.mean(costs)))
print("average runtime: {} sec".format(numpy.mean(times)))


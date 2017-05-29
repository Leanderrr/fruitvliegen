"""
BRR
it's hot
Runs the breadthfirst4 script a number of times with different genomes

Leander
"""

from breadthfirst4 import main as bestfirst
from random import shuffle

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

for i in range(0, nruns):
    shuffle(genome)
    print("\ngenome to sequence: {}".format(genome))
    bestfirst(genome, functionseq, functionmut, padding, stop, printer, plotter)
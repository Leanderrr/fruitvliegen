"""
Helper functions for the breadth first algorithm
Leander
Nina

2017-5-16
"""
import numpy as np
import time

def stepbackcleanup(genes, sollevel, throw):
    """
    This is a genome queue cleanup function, which throws away all genomes above 'throw' levels below the sollevel depth
    :param genes: A priorityQue which holds all genomes
    :param archive: A dictionary with extra information about the genomes
    :param sollevel: integer, The depth level of
    :return: updated genomes, deleted all genomes in upper 3 depth levels
    """
    i = len(genes) - 1
    while i >= 0:
        __, __, level = genes[i]
        if level > sollevel - throw:
            del genes[i]
        i -= 1

def prioritycleanup(genes, sollevel):
    """
    This function throws away a lot of genomes to make room in the memory and speed up the searching process.
    It throws away based on whether certain genomes are worse than average according to their depth level,
    but with added linear function it keeps genomes of low depth levels, this enables the search tree to go far back,
    which can enable better solutions

    :param genes: A priorityQue which holds all genomes
    :param archive: A dictionary with extra information about the genomes
    :param sollevel: integer, The depth level of the last solution, or the desired solution depth level

    :return (implicitly): updated genomes, deleted worse than average genomes, but biasing for low depth level

    """


    # Get the average priority of genomes per depth level
    meanPriorities = []
    allPriorities = []# This might be quite a killer

    for i in range(0, sollevel+2):
        allPriorities.append([])

    for i in range(len(genes)):
        priority, __,  level = genes[i]
        allPriorities[level-1].append(priority)

    for i in range(len(allPriorities)):
        # print(len(allPriorities[i]))
        if allPriorities[i]:
            # The added linearity favors low depth, keeping their best forever
            # -0.01x + 0.125 causes the first halve of 25genomes to be cut above the average score, and the deeper halve below average
            meani = np.mean(allPriorities[i]) - 0.01 * i + 0.125
            meanPriorities.append(meani)

    # print('meanPriorities')
    # print(meanPriorities)
    # print('\n')

    # Killing all above average priority genomes
    i = len(genes)-1

    while i >= 0:
        priority, __, level = genes[i]
        if level>len(meanPriorities):
            del genes[i]
        elif priority > meanPriorities[level-1]:
            del genes[i]
        i -= 1

def traceMutations(archive, mut, genelen, geneOrigin, solution):
    """
    This function traces back the genomes, from starting genome to the solution.
    After only the mutation numbers were saved in a dictionary.

    input args:
        - archive: The dictionary which holds all the genomes that were found by doing mutations.
        - mut: 3 lists which hold the meaning of mutation indexes.
        - geneOrigin: The gene at which to stop searching. (One end of the search)(a list of numbers)
        - solution: The solution, which should be in the archive (Starting point of search)(a list of numbers)

    output:
        - genes: The genomes. A list of lists
        - mutationTracker: A mutationtracker! (list of mutation indexes)
        - costs: The saved cost of the sequences
        - levels: (A list with the depth-level of the genomes found by the search (should be sequential numbers))
    """

    # Start searching from solution
    key = ".".join(str(x) for x in solution)
    gene = solution
    if len(gene) > genelen:
        gene.pop()

    # Search untill geneOrigin is found
    geneOrigin = ".".join(str(x) for x in geneOrigin)

    genes = []
    mutationTrack = []
    costs = []
    mutsum = []
    mutsum2 = []
    levels = []

    while True:
        # Find mutation and gene sequence for this key, use information to go to the next

        level = archive[key][0]
        mutation = archive[key][1]

        genes.insert(0, gene[:])
        mutationTrack.insert(0, mutation)
        levels.insert(0, level)
        costs.insert(0, archive[key][2])
        mutsum.insert(0, archive[key][3])
        mutsum2.insert(0, archive[key][4])


        # Retrace the gene created by this mutation and use it as new key
        gene[mut.start[mutation]:mut.end[mutation]] = gene[mut.start[mutation]:mut.end[mutation]][::-1]
        key = ".".join(str(x) for x in gene)
        # print("key: {}".format(key))
        # print("mutation: {}".format(mutation))
        # print("level: {}".format(level))


        if key == geneOrigin:
            # Gene origin is found
            genes.insert(0, gene[:])
            costs.insert(0, archive[key][2])
            break

    return genes, mutationTrack, costs, mutsum, mutsum2, levels
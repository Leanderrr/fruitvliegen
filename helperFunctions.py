"""
Helper functions for the breadth first algorithm
Leander
Nina

Functions:
-stepbackcleanup
-prioritycleanup
-traceMutations
-traceGenomes
-newbranch

2017-5-16
"""
import numpy as np
from mutations import mutationlist

def stepbackcleanup(genes, sollevel, throw):
    """
    This is a genome queue cleanup function,
    which throws away all genomes above 'throw' levels below the sollevel depth

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
    This function throws away a lot of genomes to make room in the memory
    and speed up the searching process.
    It throws away based on whether certain genomes are worse than average
    according to their depth level, but with added linear function it keeps
    genomes of low depth levels, this enables the search tree to go far back,
    which can enable better solutions

    :param genes: A priorityQue which holds all genomes
    :param archive: A dictionary with extra information about the genomes
    :param sollevel: integer, The depth level of the last solution

    :return (implicitly): deleted worse than average genomes

    """

    # Get the average priority of genomes per depth level
    meanPriorities = []
    allPriorities = []

    # list with lists to store all priorities
    for i in range(0, sollevel+2):
        allPriorities.append([])

    # Saving all priorities per level
    for i in range(len(genes)):
        priority, __,  level = genes[i]
        allPriorities[level-1].append(priority)

    # Taking the average priority per level
    for i in range(len(allPriorities)):
        if allPriorities[i]:
            # The added linearity favors low depth, keeping their best forever
            # -0.01*depth + 0.125 causes the first halve of 25genomes to be cut
            # above the average score, and the deeper halve below average
            meani = np.mean(allPriorities[i]) - 0.01 * i + 0.125
            meanPriorities.append(meani)

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
    This function traces back the genomes, from the solution to the geneOrigin

    Known limitations: When there were genome sequences which had overlapping parts
    (same genome and mutation),but on different depth levels, only the path with
    the lowest depth levels (the best one) can be found;
    the shorter path has overwritten the longer path.

    input args:
        - archive: The dictionary which holds all the genomes
        - mut: 3 lists which hold the meaning of mutation indexes.
        - geneOrigin: The gene at which to stop searching.(a list of numbers)
        - solution: The solution at which to start searching (a list of numbers)

    output:
        - genes: The genomes. A list of lists
        - mutationTracker: A mutationtracker! (list of mutation indexes)
        - costs: The saved cost of the sequences
        - levels: (A list with the depth-level of the genomes found by the search
                  (should be sequential numbers))
    """

    # Start searching from solution
    key = ".".join(str(x) for x in solution)
    gene = solution
    if len(gene) > genelen:
        gene.pop()

    geneOrigin = ".".join(str(x) for x in geneOrigin)

    # Variables that will be returned
    genes = []
    mutationTrack = []
    costs = []
    mutsum = []
    mutsum2 = []
    levels = []

    while True:
        # Find mutation and gene sequence for this key
        # Use information to go to the next gene

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

        if key == geneOrigin:
            # Gene origin is found
            genes.insert(0, gene[:])
            costs.insert(0, archive[key][2])
            break

    return genes, mutationTrack, costs, mutsum, mutsum2, levels


def mutationLineTest(genome, mutationTrack):
    """
    This function is used to test the outcome of a mutationTracker
    given a certain starting genome
    :param genome: The starting genome (a list of numbers)
    :param mutationTrack: The mutation tracker  which denotes which mutations
            should be done on the genome mutation indexes are based on the
            mutationlist class (a list of numbers)

    :return genes: A list of genomes which results from the requested mutationList
    """
    mut = mutationlist(len(genome))  # Get which mutations are possible on this genome
    genes = [genome]

    # Do all the mutations in the mutationTracker and save the results
    for mutation in mutationTrack:
        genome[mut.start[mutation]:mut.end[mutation]] = genome[mut.start[mutation]:mut.end[mutation]][::-1]
        genes.append(genome[:])

    return genes


def new_branch(genes, mutationTrack):
    """
    FOR DEPTHFIRST SEARCH
    Goes back to a previous level and takes a new child from there.
    args:
        genes: The sequence of genomes in the stack
        mutationTrack: The mutation tracker list
    output:
        A shorter mutationtracker and shorter genes list
        A new child
        New current mutation
    """

    if len(genes) == 1:
        print("\n\nSTACK EMPTY: All branches died out due to pruning and doubles!!!")
        child = genes[-1][:]
        mutation = 0
        Go = False
        return child, mutation, Go

    genes.pop()
    child = genes[-1][:]
    mutation = mutationTrack.pop() + 1
    return child, mutation, True


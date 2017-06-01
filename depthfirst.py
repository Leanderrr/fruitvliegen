"""
Functions for search algorithms

Leander
Nina
"""
from mutations import mutationlist

def new_branch(genes, mutationTrack):
    """
    Goes back to a previous level and takes a new child from there
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


def mutationLineTest(genome, mutationTrack):
    """
    This function is used to test the outcome of a mutationTracker given a certain starting genome
    input args:
        genome: The starting genome (a list of numbers)
        mutationTrack: The mutation tracker which denotes which mutations should be done on the genome
            mutation indexes are based on the mutationlist class (a list of numbers)

    output:
        genes: A list of genomes which results from the requested mutationList (a list of lists of numbers)
    """
    mut = mutationlist(len(genome)) # Get which mutations are possible on this genome
    genes = [genome]

    # Do all the mutations in the mutationTracker and save the results
    for mutation in mutationTrack:
        genome[mut.start[mutation]:mut.end[mutation]] = genome[mut.start[mutation]:mut.end[mutation]][::-1]
        genes.append(genome[:])

    return genes
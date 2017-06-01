"""
First depth first search algorithm to find a mutation sequence that turns one 'genome' into another
MET ARCHIEF

Leander
Nina

started: 2017-5-2
"""
from mutations import mutationlist
from helperFunctions import new_branch
from plotters import plotMutations
import time


def main(geneOrigin=[5, 2, 1, 4, 3], maxDepth=4, printer=True, plotter=True):
    geneLength = len(geneOrigin)
    genes = []
    genes.append(geneOrigin)

    # Create solution array
    solution = []
    for i in range(1, geneLength+1):
        solution.append(i)

    mutationTrack = [-1] # This keeps track of how many mutations have been tried for a child

    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)

    # Depth first search
    archive = dict()
    archive["".join(str(x) for x in geneOrigin)] = True
    Go = True
    doubleCounter = 0
    tstart = time.time()
    while Go:
        print(len(genes))

        # Create Child
        child = genes[-1][:]
        mutation = mutationTrack.pop() + 1

        if len(genes) >= maxDepth:
            # Stop with branch when reaching maxDepth
            child, mutation, Go = new_branch(genes, mutationTrack)

        while mutation >= mut.max:            # Go up one level and continue with the other mutation
            child, mutation, Go = new_branch(genes, mutationTrack)

        mutationTrack.append(mutation)  # mutation  kept track of
        # Mutate the child, according to the latest mutation of this 'node'
        child[mut.start[mutation]:mut.end[mutation]] = child[mut.start[mutation]:mut.end[mutation]][::-1]

        key = "".join(str(x) for x in child)

        if child == solution:
            # Check whether child is solutions
            Go = False
            genes.append(child[:])

        # Check whether child is unique or not
        elif archive.get(key, False) and (len(mutationTrack) > archive.get(key, 100)):
            doubleCounter += 1
        else:
            # Add child to archive if it is unique and not a solution
            archive[key] = len(mutationTrack)
            genes.append(child[:])
            mutationTrack.append(-1)

    tduration = time.time() - tstart
    print("{0:.3f}".format(tduration))

    if printer:
        print('number of genomes in archive: {}'.format(len(archive)))
        print('# of double found sequences:  {}'.format(doubleCounter))

        i = 0
        for gene in genes:
            print("{} {}".format(i, gene))
            i += 1

    print("final mutation tracker: {}".format(mutationTrack))

    if plotter:
        plotMutations(genes, mutationTrack, mut)

if __name__ == '__main__':
    main()
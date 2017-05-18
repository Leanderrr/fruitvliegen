"""
First breadth first search algorithm to find a mutation sequence that turns one 'genome' into another
MET ARCHIEF

Leander
Nina
started: 2017-5-15
"""

from mutations import mutationlist
from breadthfirst import traceMutations
from depthfirst import plotMutations
from queue import Queue
import time

def main(geneOrigin =  [5,2,6,1,4,3,7,11,8,9,10], printer = True, plotter = True):

    geneLength = len(geneOrigin)
    genes = Queue()
    genes.put(geneOrigin)

    # Create solution array
    solution = []
    for i in range(1,geneLength+1):
        solution.append(i)

    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)
    # print("max mutations per mother: {}".format(mut.max))

    # Breadth First Search
    archive = dict()
    key = ".".join(str(x) for x in geneOrigin)
    archive[key] = [0] # The value is the depth level of this gene sequence
    Go = True
    doubleCounter = 0
    tstart = time.time()

    while Go:
        # stap 1: Alle mogelijke kinderen maken en opslaan - checken of een van de kinderen de oplossing is. (dat is een grote stap)

        mother = genes.get()
        motherkey = ".".join(str(x) for x in mother)

        level = archive[motherkey][0] + 1

        # print(archive[motherkey])

        # mutate the child - add to queue if not already in archive nor solution of the problem
        for i in range(0, mut.max):

            child = mother[:]
            child[mut.start[i]:mut.end[i]] = child[mut.start[i]:mut.end[i]][::-1]
            key = ".".join(str(x) for x in child)
            # print(key)
            # check if child is the solution
            if child == solution:
                Go = False
                # print("wiehoe")
                genes.put(child)
                archive[key] = [level, i]
                break

            # check if child is already in the archive - if so don't add this child to the queu
            elif (archive.get(key, False) != False):
                doubleCounter += 1

            # child is not the solution nor in archive - so should be added to the end of thequeu and archive
            else:
                genes.put(child)
                archive[key] = [level, i]

    tduration = time.time() - tstart
    print("{0:.3f}".format(tduration))

    genes, mutationTrack, levels = traceMutations(archive, mut, geneOrigin, solution)

    if printer == True:
        i = 0
        for gene in genes:
            print("{} {}".format(i, gene))
            i += 1

        print('number of genomes in archive: {}'.format(len(archive)))
        print('# of double found sequences:  {}'.format(doubleCounter))

    print("mutation tracker: {}".format(mutationTrack))
    # print("depth level:      {}".format(levels))

    if plotter == True:
        plotMutations(genes, mutationTrack, mut)

if __name__ == '__main__':
    main()
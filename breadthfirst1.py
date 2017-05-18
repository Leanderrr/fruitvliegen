"""
First breadth first search algorithm to find a mutation sequence that turns one 'genome' into another
MET ARCHIEF
EN PRIORITY CUE
Deze is heel snel in de eerste oplossing vinden

Leander
Nina

started: 2017-5-15
"""

from mutations import mutationlist
from breadthfirst import traceMutations
from queue import PriorityQueue
from depthfirst import plotMutations
import costfunction
import costfunction2
import costfunction1
import costfunction4
import costfunction5
import time

def main(geneOrigin =  [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9], printer = True, plotter = True):

    geneLength = len(geneOrigin)
    genes = PriorityQueue()
    priority = costfunction4.main(geneOrigin)
    # print("priority = {}".format(priority))
    genes.put((priority, geneOrigin))

    # Create solution array
    solution = []
    for i in range(1, geneLength + 1):
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

        priority, mother = genes.get()
        #print("mother = {}".format(mother))
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
                priority = costfunction4.main(child)
                genes.put((priority, child))
                archive[key] = [level, i]
                break

            # check if child is already in the archive - if so don't add this child to the queu
            elif (archive.get(key, False) != False):
                doubleCounter += 1

            # child is not the solution nor in archive - so should be added to the end of the queu and archive
            else:
                priority = costfunction4.main(child)
                genes.put((priority, child))
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

    if plotter == True:
        plotMutations(genes, mutationTrack, mut)


if __name__ == '__main__':
    main()
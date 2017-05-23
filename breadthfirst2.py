"""
First breadth first search algorithm to find a mutation sequence that turns one 'genome' into another
MET ARCHIEF
EN PRIORITY CUE
EN stopt niet als ie één oplossing heeft gevonden
Deze is heel snel in de eerste oplossing vinden

Leander
Nina

started: 2017-5-15
"""

from mutations import mutationlist
from breadthfirst import traceMutations
from queue import PriorityQueue
from depthfirst import plotMutations
from cost import cost
import time

# [16,2,9,25,8,24,14,21,11,10,3,4,13,22,23,19,15,18,7,1, 12, 5, 6, 17, 20] # Fonsos sequentie
#  [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9] # Official sequenty
def main(geneOrigin =  [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9], printer = True, plotter = True):

    function = 5 # The costfunction used!
    stop = 10 # Stop after this many solutions are found
    prunelevel = 25
    geneLength = len(geneOrigin)
    genes = PriorityQueue()
    priority = cost(function, geneOrigin)
    # print("priority = {}".format(priority))
    genes.put((priority, geneOrigin))

    # Create solution array
    solution = []
    for i in range(1, geneLength + 1):
        solution.append(i)

    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)
    # print("max mutations for this genome: {}".format(mut.max))

    # Breadth First Search
    archive = dict()
    solnum = 0
    key = ".".join(str(x) for x in geneOrigin)
    archive[key] = [0] # The value is the depth level of this gene sequence
    Go = True
    doubleCounter = 0
    tstart = time.time()

    while (not genes.empty()) and (Go == True):
        # stap 1: Alle mogelijke kinderen maken en opslaan - checken of een van de kinderen de oplossing is. (dat is een grote stap)

        priority, mother = genes.get()
        #print("mother = {}".format(mother))
        motherkey = ".".join(str(x) for x in mother)
        level = archive[motherkey][0] + 1

        if level > prunelevel:
            genes.get()

        else:
            # print(archive[motherkey])

            # mutate the child - add to queue if not already in archive nor solution of the problem
            for i in range(0, mut.max):
                child = mother[:]
                child[mut.start[i]:mut.end[i]] = child[mut.start[i]:mut.end[i]][::-1]
                key = ".".join(str(x) for x in child)
                # print(key)

                # check if child is the solution
                if child == solution:
                    priority = cost(function, child)
                    # genes.put((priority, child))
                    key = ".".join((key, str(solnum))) # Remember which solution this was in the library
                    print("sol {:<3}: level:  {}".format(solnum, level))
                    print(genes.qsize())
                    archive[key] = [level, i, priority]
                    solnum += 1
                    prunelevel = level
                    if solnum == stop:
                        Go = False

                # check if child is already in the archive - if so don't add this child to the queue
                elif (archive.get(key, False) != False) and archive.get(key, 100)[0] < level:
                    # print("earlier level {}, current level {}".format((archive.get(key, False)[0]), level))
                    doubleCounter += 1

                # child is not the solution nor in archive - so should be added to the end of the queue and archive
                else:
                    priority = cost(function, child)
                    genes.put((priority, child))
                    archive[key] = [level, i, priority]


    tduration = time.time() - tstart
    print("{0:.3f}".format(tduration))

    if printer == True:
        print('number of genomes in archive: {}'.format(len(archive)))
        print('# of double found sequences:  {}'.format(doubleCounter))

    # Retrace which mutations were done to get the solutions
    for i in range(0, solnum):
        solutioni = solution[:]
        solutioni.extend([i])
        genes, mutationTrack, levels = traceMutations(archive, mut, geneLength, geneOrigin, solutioni)

        print("{:<3}. mutation tracker: {}".format(i, mutationTrack))

    if plotter == True:
        plotMutations(genes, mutationTrack, mut)


if __name__ == '__main__':
    main()
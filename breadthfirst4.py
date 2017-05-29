"""
First breadth first search algorithm to find a mutation sequence that turns one 'genome' into another
MET ARCHIEF
EN PRIORITY CUE
EN stopt niet als ie één oplossing heeft gevonden
EN gooit de helft van de queue weg
Deze is heel snel in de eerste oplossing vinden

Leander
Nina

started: 2017-5-15
"""

from mutations import mutationlist
from breadthfirst import traceMutations
from breadthfirst import prioritycleanup
from breadthfirst import stepbackcleanup
from heapq import *
from depthfirst import plotMutations
from cost import cost
import time
import random

#  [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9] # Official sequency
def main(geneOrigin=False, functionseq=1, functionmut=0, padding=True, stop=100, printer = True, plotter = True):
    if isinstance(geneOrigin, bool):
        geneOrigin = [1, 2, 11, 19, 6, 10, 7, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
        random.shuffle(geneOrigin)

    # geneOrigin = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
    prunelevel = len(geneOrigin)
    mutsummax = 200
    print(geneOrigin)
    # Create solution array
    geneLength = len(geneOrigin)
    solution = []
    for i in range(1, geneLength + 1):
        solution.append(i)

    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)

    # print("max mutations for this genome: {}".format(mut.max))
    genes = []
    priority, __, __ = cost(functionseq, padding, geneOrigin)
    level = 0
    # print("priority = {}".format(priority))
    heappush(genes, (priority, geneOrigin, level))

    # Best First Search
    archive = dict()
    solnum = 0
    key = ".".join(str(x) for x in geneOrigin)

    priority, __, __ = cost(functionseq, padding, geneOrigin)
    archive[key] = [level, 0, priority, 0,0] # 1st value: deth level, 2nd value: last mutation, 3th value: priority, 4th value: sum of mutations
    Go = True
    doubleCounter = 0
    tstart = time.time()

    while (not len(genes)==0) and (Go == True):
        # stap 1: Alle mogelijke kinderen maken en opslaan - checken of een van de kinderen de oplossing is. (dat is een grote stap)

        priority, mother, level = heappop(genes)
        #print("mother = {}".format(mother))
        motherkey = ".".join(str(x) for x in mother)

        level += 1
        mutsum = archive[motherkey][3]

        if level > prunelevel+2 or mutsum >= mutsummax :
            heappop(genes)

        else:
            # print(archive[motherkey])

            # mutate the child - add to queue if not already in archive nor solution of the problem
            for i in range(0, mut.max):
                child = mother[:]
                mutsum = archive[motherkey][3]
                mutsum2 = archive[motherkey][4]
                child[mut.start[i]:mut.end[i]] = child[mut.start[i]:mut.end[i]][::-1]
                key = ".".join(str(x) for x in child)
                # print(key)

                # check if child is the solution
                if child == solution:
                    priority, mutsum, mutsum2 = cost(functionseq, padding, child, mutsum, mutsum2, functionmut, i, mut, level)
                    key = ".".join((key, str(solnum))) # Remember which solution this was in the library
                    print("sol {:<3}: level:  {}".format(solnum, level))
                    archive[key] = [level, i, priority, mutsum, mutsum2]

                    thissol = solution[:]
                    thissol.extend([solnum])
                    genesT, mutationTrackT, costsT, mutsumT, mutsum2T, __ = traceMutations(archive, mut, geneLength, geneOrigin, thissol)
                    print("mutationtracker:{}".format(mutationTrackT))
                    print("cost:           {}".format(costsT[-1]))
                    print("mutsum          {}".format(mutsumT[-1]))
                    print("mutsum2         {}".format(mutsum2T[-1]))

                    # plotMutations(genesT, mutationTrackT, mut)

                    stepbackcleanup(genes, level, 4)
                    prioritycleanup(genes, level)

                    solnum += 1
                    prunelevel = level
                    mutsummax = mutsum+1
                    if solnum == stop:
                        Go = False

                # check if child is already in the archive - if so don't add this child to the queue
                elif (archive.get(key, False) != False) and (archive.get(key, 100)[0] < level):
                    # print("earlier level {}, current level {}".format((archive.get(key, False)[0]), level))
                    doubleCounter += 1

                # child is not the solution nor in archive - so should be added to the end of the queue and archive
                else:
                    priority, mutsum, mutsum2 = cost(functionseq, padding, child, mutsum, mutsum2, functionmut, i, mut, level)
                    heappush(genes, (priority, child, level))
                    archive[key] = [level, i, priority, mutsum, mutsum2]

            # Pruning that keeps low levels
            if len(genes) > 750000:
                prioritycleanup(genes, prunelevel)
                # print(len(genes))

            # Pruning that throws away low levels, and thus cannot dramatically change its route after some time
            # Remove a part of the queue
            # cutat = 10000 # Cut at x many genes
            # if len(genes)>cutat:
            #     cut = len(genes)-cutat
            #     del genes[-cut::]
            #
            # heapify(genes)


    tduration = time.time() - tstart
    print("duration: {0:.3f} sec".format(tduration))

    if printer == True:
        print('number of genomes in archive: {}'.format(len(archive)))
        print('# of double found sequences:  {}'.format(doubleCounter))

    # Retrace which mutations were done to get the solutions
    for i in range(0, solnum):
        solutioni = solution[:]
        solutioni.extend([i])

        genes, mutationTrack, costs, mutsum, mutsum2, levels = traceMutations(archive, mut, geneLength, geneOrigin, solutioni)
        if printer == True:
            print("{:<2} mutations: {}".format(i, mutationTrack))
            print("{:<2} costs:     {}".format(i, costs))
            print("{:<2} mutsums:   {}".format(i, mutsum))
            print("{:<2} mutsums2:  {}".format(i, mutsum2))

        if plotter == True:
            plotMutations(genes, mutationTrack, mut)

    return mutsum[-1], mutsum2[-1], levels[-1], costs[1], tduration


if __name__ == '__main__':
    main()
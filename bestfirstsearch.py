"""
Best First Search that explores the state space

Includes an archive 
Queue is ordered based on costfunction in cost.py
Stops at the stop level 
Throws away half of the queue
Output in graph -> the darker the shade of the flip line, the longer the mutation

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

# given genome of D. miranda
#[23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

def main(geneOrigin=False, functionseq=1, functionmut=3, padding=True, stop=11, printer = True, plotter = True):
    """
    :param geneOrigin: The sequence of genes to start with
    :param functionseq: The sequence cost function (select it with an integer)
    :param functionmut: The mutation cost function (select it with an integer)
    :param padding: Activate padding around the genome sequence for the costfunction (True or False)
    :param stop: Stop after this many solutions are found (integer)
    :param printer: Activate more printed output (True or False)
    :param plotter: Activate the plots! Only when the program stops, one at a time (True or False)
    :return:
    """
    if isinstance(geneOrigin, bool):
        geneOrigin = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
        # random.shuffle(geneOrigin)

    prunelevel = len(geneOrigin)
    mutsummax = 200 # Sum of mutation lengths max, if exceeded, genes get pruned

    # Create solution array
    geneLength = len(geneOrigin)
    solution = []
    for i in range(1, geneLength + 1):
        solution.append(i)

    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)

    # Create genome queue and fill in the starting gene
    genes = []
    priority, __, __ = cost(functionseq, padding, geneOrigin)
    level = 0
    heappush(genes, (priority, geneOrigin, level))

    # Best First Search
    archive = dict()
    solnum = 0
    key = ".".join(str(x) for x in geneOrigin)

    priority, __, __ = cost(functionseq, padding, geneOrigin)
    # 1st value: deth level, 2nd: last mutation, 3th: priority, 4th: sum of mutations
    archive[key] = [level, 0, priority, 0,0]
    Go = True
    doubleCounter = 0
    tstart = time.time()

    while (not len(genes)==0) and (Go == True):

        # Make all possible children and save them
        priority, mother, level = heappop(genes)
        #print("mother = {}".format(mother))
        motherkey = ".".join(str(x) for x in mother)

        level += 1
        mutsum = archive[motherkey][3]

        if level > prunelevel or mutsum >= mutsummax :
            heappop(genes)

        else:
            # mutate the child - add to queue if not already in archive nor solution of the problem
            for i in range(0, mut.max):
                child = mother[:]
                mutsum = archive[motherkey][3]
                mutsum2 = archive[motherkey][4]
                child[mut.start[i]:mut.end[i]] = child[mut.start[i]:mut.end[i]][::-1]
                key = ".".join(str(x) for x in child)

                # check if child is the solution
                if child == solution:
                    priority, mutsum, mutsum2 = cost(functionseq, padding, child, mutsum,
                                                mutsum2, functionmut, i, mut, level)

                    # Remember which solution this was in the library
                    key = ".".join((key, str(solnum)))
                    archive[key] = [level, i, priority, mutsum, mutsum2]

                    # Print informat from this solution
                    thissol = solution[:]
                    thissol.extend([solnum])
                    genesT, mutationTrackT, costsT, mutsumT, mutsum2T, __ = traceMutations(archive,
                                                                                           mut,
                                                                                           geneLength,
                                                                                           geneOrigin,
                                                                                           thissol)

                    print("sol {:<3}: level:  {}".format(solnum, level))
                    print("mutationtracker:{}".format(mutationTrackT))
                    print("mutsum          {}".format(mutsumT[-1]))
                    print("mutsum2         {}".format(mutsum2T[-1]))

                    # Delete a part of the genome queue
                    stepbackcleanup(genes, level, 7)
                    prioritycleanup(genes, level)

                    solnum += 1
                    prunelevel = level
                    mutsummax = mutsum+1

                    # Stop program when desired amount of solutions is found
                    if solnum == stop:
                        Go = False

                # check if child is already in the archive - if so don't add this child to the queue
                elif (archive.get(key, False) != False) and (archive.get(key, 100)[0] <= level):
                    # print("earlier level {}, current level {}".format((archive.get(key, False)[0]), level))
                    doubleCounter += 1

                # child is not the solution nor in archive - so should be added to the end of the queue and archive
                else:
                    priority, mutsum, mutsum2 = cost(functionseq, padding, child, mutsum,
                                                     mutsum2, functionmut, i, mut, level)
                    heappush(genes, (priority, child, level))
                    archive[key] = [level, i, priority, mutsum, mutsum2]

            # Pruning that keeps low levels
            if len(genes) > 10000:
                prioritycleanup(genes, prunelevel)
                # print(len(genes))
                if time.time() - tstart > 60:
                    Go = False


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

    minmutsum = 1000
    minmutsum2 = 1000
    minlevel = 100

    # Retrace which mutations were done to get the solutions
    for i in range(0, solnum):
        solutioni = solution[:]
        solutioni.extend([i])

        genes, mutationTrack, costs, mutsum, mutsum2, levels = traceMutations(archive,
                                                                              mut, geneLength,
                                                                              geneOrigin, solutioni)

        # Output the best result
        if mutsum[-1] < minmutsum and mutsum2[-1] < minmutsum2:
            same = True
            minmutsum = mutsum[-1]
            minmutsum2 = mutsum2[-1]
            outmutation1 = mutationTrack
        elif mutsum[-1] < minmutsum:
            minmutsum = mutsum[-1]
            outmutation1 = mutationTrack
            same = False
        elif mutsum2[-1] < minmutsum2:
            minmutsum2 = mutsum2[-1]
            same = False

        if levels[-1] < minlevel:
            minlevel = levels[-1]
            outcosts = costs[1]
            outmutation2 = mutationTrack
            solutionN = i

        if printer == True:
            print("{:<2} mutations: {}".format(i, mutationTrack))
            print("{:<2} costs:     {}".format(i, costs))
            print("{:<2} mutsums:   {}".format(i, mutsum))
            print("{:<2} mutsums2:  {}".format(i, mutsum2))

        if plotter == True:
            plotMutations(genes, mutationTrack, mut)

    return (minmutsum, minmutsum2, minlevel, outcosts,
            outmutation1, outmutation2, same, solutionN, tduration)


if __name__ == '__main__':
    main()
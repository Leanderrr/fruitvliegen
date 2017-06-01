"""
Best First Search that explores the state space

Includes an archive
Queue is ordered based on costfunctions in cost.py
Stops at the stop level
stops after stoptime seconds
Throws away half of the queue, per level
graphical Output provided by the plotters functions :)

Leander de Kraker
Nina Cialdella

started: 2017-5-15
"""

from mutations import mutationlist
from helperFunctions import traceMutations
from helperFunctions import prioritycleanup
from helperFunctions import stepbackcleanup
from plotters import plotMutations
from heapq import *
from cost import cost
import time

def main(geneOrigin=False, functionseq=1, functionmut=3, padding=True, stop=10, printer = True, plotter = True):
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
        # Genome of D. Miranda
        geneOrigin = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

    prunelevel = len(geneOrigin)
    mutsummax = 200  # Sum of mutation lengths max, if exceeded, genes get pruned
    stoptime = 60   # Stop searching after this many seconds

    # Create solution genome array
    geneLength = len(geneOrigin)
    solution = []
    for i in range(1, geneLength + 1):
        solution.append(i)

    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)

    # Create genome queue and fill in the starting gene
    level = 0
    solnum = 0  # 0 solutions as of yet
    genes = []
    priority, __, __ = cost(functionseq, padding, geneOrigin)
    heappush(genes, (priority, geneOrigin, level))

    archive = dict()
    key = ".".join(str(x) for x in geneOrigin)

    priority, __, __ = cost(functionseq, padding, geneOrigin)
    # 1st value: depth level, 2nd: last mutation, 3th: priority, 4th: sum of mutations
    archive[key] = [level, 0, priority, 0, 0]
    Go = True
    doubleCounter = 0
    tstart = time.time()

    # Run search!
    while genes and Go:
        priority, mother, level = heappop(genes)
        motherkey = ".".join(str(x) for x in mother)

        level += 1
        mutsum = archive[motherkey][3]

        if level > prunelevel or mutsum >= mutsummax :
            # pop and go to next genome if this one is getting too long or deep
            heappop(genes)

        else:
            # Make all possible children and save them
            for i in range(0, mut.max):
                child = mother[:]
                mutsum = archive[motherkey][3]
                mutsum2 = archive[motherkey][4]

                # mutation i for this child
                child[mut.start[i]:mut.end[i]] = child[mut.start[i]:mut.end[i]][::-1]
                key = ".".join(str(x) for x in child)

                # check if child is the solution
                if child == solution:
                    priority, mutsum, mutsum2 = cost(functionseq, padding, child,
                                                     mutsum, mutsum2, functionmut,
                                                     i, mut, level)

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
                    doubleCounter += 1

                # child is not the solution nor in archive - so should be added to the queue and archive
                else:
                    priority, mutsum, mutsum2 = cost(functionseq, padding, child, mutsum,
                                                     mutsum2, functionmut, i, mut, level)
                    heappush(genes, (priority, child, level))
                    archive[key] = [level, i, priority, mutsum, mutsum2]

            # Pruning that keeps low levels
            if len(genes) > 100000:
                prioritycleanup(genes, prunelevel)
                # Stop searching solutions after 2 minutes
                if time.time() - tstart > stoptime:
                    Go = False


    tduration = time.time() - tstart
    print("duration: {0:.3f} sec".format(tduration))

    if printer == True:
        print('number of genomes in archive: {}'.format(len(archive)))
        print('# of double found sequences:  {}'.format(doubleCounter))

    minmutsum = 99999
    minmutsum2 = 99999
    minlevel = 999999

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
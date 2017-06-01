"""
This code will try to sort an array by flipping parts of the unsorted array
First 'algorithm' to get the genome of the Miranda from the genome of Melanogaster

2017-4-13
Leander de Kraker
"""

from plotters import plotMutationsflipsort as plotMutations
import time

def main(geneOrigin =  False, plot = True, printer = True):
    if geneOrigin == False:
        geneOrigin = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

    mutsum = 0
    mutsum2 = 0

    gene = geneOrigin
    genes = []
    solution = range(1, len(gene)+1) # Genome of Miranda

    flips = [] # Variable that will remember which flips have been done

    flip = []
    cumlength = 0

    # print("Genome sequence: ")
    tstart = time.time()
    # Sorting the genome
    for i in range(len(gene)):
        # If the correct gene is not at ith position FLIP
        if gene[i] != solution[i]:
            flip = [i, gene.index(solution[i])+1]

            if printer == True:
                print("{0:<3}{1}".format(i, gene))

            # FLIP
            genes.append(gene[:])
            gene[flip[0]:flip[1]] = gene[flip[0]:flip[1]][::-1]

            mutsum += flip[1] - flip[0]
            mutsum2 += 0.5 * pow((flip[1]-flip[0]), 2)
            flips.append(flip)

    # Printing showing mutations
    genes.append(gene[:])
    if printer == True:
        print("fin{}".format(gene))
        print("\nflip sequence")
        print("n   : start gen: length of flip")
        for i in range(len(flips)):
            print("{0:<4}: {1:<9}: {2:<4}".format((i+1),flips[i][0],flips[i][1]))

        print("Number of mutations:  {}".format(len(flips)))
        print("mutsum  (n)      = {}".format(mutsum))
        print("mutsum2 (0.5*n^2)= {}".format(mutsum2))

    tduration = time.time() - tstart
    print("time: {0:.3f}sec".format(tduration))

    # Figure showing mutations
    if plot == True:
        plotMutations(genes, flips)

    return len(flips), mutsum, mutsum2


if __name__ == "__main__":
    main()
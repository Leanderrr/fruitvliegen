"""
This code will try to sort an array by flipping parts of the unsorted array
First 'algorithm' to get the genome of the Miranda from the genome of Melanogaster

2017-4-13
Leander de Kraker
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
from numpy import linspace
import time

def main(geneOrigin = [16,2,9,25,8,24,14,21,11,10,3,4,13,22,23,19,15,18,7,1, 12, 5, 6, 17, 20], plot = True, printer = True):
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

    tduration = time.time() - tstart
    print("{0:.3f}".format(tduration))

    # Figure showing mutations
    if plot == True:
        cm_subsection = linspace(0, 1, len(genes[0]) + 2)
        colors = [cm.summer(x) for x in cm_subsection]
        colors2 = [cm.Reds(x) for x in cm_subsection]

        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111)

        y = 0
        for genome in genes:
            # Print genome text in figure
            x = 0
            for gen in genome:
                ax.text(x, y, '{}, '.format(gen))
                # Add colored rectangle showing gen value height
                ax.add_patch(patches.Rectangle(
                    (x - 0.05, y - 0.1), 0.25, 1,
                    facecolor=(colors[gen][0], colors[gen][1], colors[gen][2], 0.7),
                    edgecolor="none"))
                x += 1 / 4
            y += 1

        # Diagonal lines!
        for i in range(len(flips)):
            x1 = (flips[i][0]+0.5) / 4 - 0.05
            x2 = (flips[i][1]-0.5) / 4 - 0.05
            y1 = i + 0.8
            y2 = i + 0.9
            ax.plot([x1, x2], [y1, y2], color=colors2[flips[i][1]-flips[i][0]])
            ax.plot([x1, x2], [y2, y1], color=colors2[flips[i][1]-flips[i][0]])

        plt.ylabel("mutation (n)")
        plt.xlabel("genome sequence")
        plt.title("mutation sequence. nr of mutations = {}".format(len(flips)))
        plt.tick_params(
            axis='x',
            which='both',  # both major and minor ticks are affected
            bottom='off',  # ticks along the bottom edge are off
            top='off',  # ticks along the top edge are off
            labelbottom='off')  # labels along the bottom edge are off
        ax.axis([-0.05, len(genes[0]) / 4, -0.1, len(genes)])
        plt.show()

    return len(flips), mutsum, mutsum2


if __name__ == "__main__":
    main()
"""
This code will try to sort an array by flipping parts of the unsorted array
First 'algorithm' to get the genome of the Miranda from the genome of Melanogaster

2017-4-13
Leander de Kraker
"""
import matplotlib.pyplot as plt
import time

def main(geneOrigin = [16,2,9,25,8,24,14,21,11,10,3,4,13,22,23,19,15,18,7,1, 12, 5, 6, 17, 20], plot = True, printer = True):
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
            genes.append(gene[:])
            gene[flip[0]:flip[1]] = gene[flip[0]:flip[1]][::-1]

            #flip[1] = flip[1]-flip[0] # Calculate length of flip
            cumlength += flip[1]
            flips.append(flip)

    # Printing showing mutations
    genes.append(gene[:])
    if printer == True:
        print("fin{}".format(gene))
        print("\nflip sequence")
        print("n   : start gen: length of flip")
        for i in range(len(flips)):
            print("{0:<4}: {1:<9}: {2:<4}".format((i+1),flips[i][0],flips[i][1]))

        # print("\nCumulative length of flips: {}".format(cumlength))
        print("Number of mutations:  {}".format(len(flips)))

    tduration = time.time() - tstart
    print("{0:.3f}".format(tduration))

    # Figure showing mutations
    if plot == True:
        fig = plt.figure(figsize=(10,15))
        plt.title("mutation sequence")
        ax = fig.add_subplot(111)
        for i in range(len(genes)):
            for j in range(len(genes[i])):
                ax.text(j/4, i, '{},'.format(genes[i][j]))

        for i in range(len(flips)):
            ax.plot([(flips[i][0]+0.5)/4, (flips[i][1]-0.5)/4], [i+0.3, i+0.9], color='g')
            ax.plot([(flips[i][0]+0.5)/4, (flips[i][1]-0.5)/4], [i+0.9, i+0.3], color='g')

        plt.ylabel("mutation (n)")
        ax.axis([-0.5, 7, -0.5, len(genes)])
        plt.show()

if __name__ == "__main__":
    main()
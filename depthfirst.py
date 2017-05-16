"""
Functions for search algorithms

Leander
Nina
"""
import matplotlib.pyplot as plt

def new_branch(genes, mutationTrack):
    """
    Goes back to a previous level and takes a new child from there
    args:
        genes: The sequence of genomes in the stack
        mutationTrack: The mutation tracker list
    output:
        A shorter mutationtracker and shorter genes list
        A new child
        New current mutation
    """
    genes.pop()
    child = genes[-1][:]
    mutation = mutationTrack.pop() + 1
    return child, mutation


def plotMutations(genes, mutationTrack, mut):
    """
    Plots the mutation sequence and gene sequence fancy-fully
    args:
        genes: A list of genomes to print
        mutationTrack: The mutations that were done
        mut: The meaning of mutations (object with 3 fields created in the mutationlist function)
    """
    fig = plt.figure(figsize=(10, 15))
    plt.title("mutation sequence")
    ax = fig.add_subplot(111)
    i = 0
    for genome in genes:
        # Print genome text in figure
        j = 0
        for gen in genome:
            ax.text(j/4, i, '{}, '.format(gen))
            j += 1
        i += 1

    i = 0
    for mutation in mutationTrack:
        # Plot mutation lines
        x1 = (mut.start[mutation] + 0.25)/4
        x2 = (mut.end[mutation] - 1 + 0.25)/4
        y1 = i + 0.3
        y2 = i + 0.9
        i += 1
        ax.plot([x1, x2], [y1, y2], color='g')
        ax.plot([x1, x2], [y2, y1], color='g')


    plt.ylabel("mutation (n)")
    ax.axis([-0.5, len(genes)/2, -0.5, len(genes)])
    plt.show()
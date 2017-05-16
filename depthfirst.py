"""
Functions for search algorithms

Leander
Nina
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
from numpy import linspace


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
    cm_subsection = linspace(0, 1, len(genes[0])+2)
    colors = [cm.summer(x) for x in cm_subsection]


    fig = plt.figure(figsize=(10, 15))
    plt.title("mutation sequence")
    ax = fig.add_subplot(111)
    y = 0
    for genome in genes:
        # Print genome text in figure
        x = 0
        for gen in genome:
            ax.text(x, y, '{}, '.format(gen))
            # Add colored rectangle showing gen value height
            ax.add_patch(patches.Rectangle(
                (x-0.125, y-0.1), 0.25, 0.25,
                facecolor=(colors[gen][0], colors[gen][1], colors[gen][2],0.7),
                edgecolor="none"))
            x += 1/4
        y += 1

    i = 0
    for mutation in mutationTrack:
        # Plot mutation lines
        x1 = (mut.start[mutation] + 0.15)/4
        x2 = (mut.end[mutation] - 1 + 0.15)/4
        y1 = i + 0.15
        y2 = i + 0.9
        i += 1
        ax.plot([x1, x2], [y1, y2], color=colors[mut.length[mutation]+1], linewidth=3)
        ax.plot([x1, x2], [y2, y1], color=colors[mut.length[mutation]+1], linewidth=3)


    plt.ylabel("mutation (n)")
    ax.axis([-0.25, len(genes)/2, -0.5, len(genes)])
    plt.show()
"""
The path from genome to genome needs some nice plotting
2017-6-1

Leander de Kraker
The flipsorter and other algorithms need slightly different plotters,
so the function is split up into multiple portions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
from numpy import linspace


def plotMutations(genes, mutationTrack, mut):
    """
    Plots the mutation sequence and gene sequence fancy-fully
    args:
        genes: A list of genomes to print
        mutationTrack: The mutations that were done
        mut: The meaning of mutations (object with 3 fields)
    """

    ax, colors, colors2 = initplot(genes)
    plotgenes(ax, genes, colors)

    # Diagonal lines!
    i = 0
    for mutation in mutationTrack:
        x1 = (mut.start[mutation])/4 - 0.05
        x2 = (mut.end[mutation])/4 - 0.05
        y1 = i + 0.8
        y2 = i + 0.9
        i += 1
        ax.plot([x1, x2], [y1, y2], color=colors2[mut.length[mutation]+1], linewidth=1.5)
        ax.plot([x1, x2], [y2, y1], color=colors2[mut.length[mutation]+1], linewidth=1.5)

    plotlabels(ax, genes, len(mutationTrack))


def plotMutationsflipsort(genes, flips):
    """
    The flipsorter does not use mut for the meaning of flips,
    so it needs a slightly different plotter
    :param genes: The genomes that need to get plotted
    :param flips: The flips done on the genome
    :return: A nice plot
    """
    ax, colors, colors2 = initplot(genes)
    plotgenes(ax, genes, colors)

    # Diagonal lines!
    for i in range(len(flips)):
        x1 = (flips[i][0] + 0.5) / 4 - 0.05
        x2 = (flips[i][1] - 0.5) / 4 - 0.05
        y1 = i + 0.8
        y2 = i + 0.9
        ax.plot([x1, x2], [y1, y2], color=colors2[flips[i][1] - flips[i][0]])
        ax.plot([x1, x2], [y2, y1], color=colors2[flips[i][1] - flips[i][0]])

    plotlabels(ax, genes, len(flips))


def initplot(genes):
    """
    Starts a figure and initiates colors
    :param genes:
    :return: axis handle, colors for the genome values and colors for the lines
    """
    cm_subsection = linspace(0, 1, len(genes[0]) + 2)
    colors = [cm.summer(x) for x in cm_subsection]
    colors2 = [cm.Reds(x) for x in cm_subsection]

    fig = plt.figure(figsize=(10, 15))
    ax = fig.add_subplot(111)

    return ax, colors, colors2


def plotgenes(ax, genes, colors):
    """
    Plots the genomes with fancy colors!
    :param ax: the axis initiated by plotinit
    :param genes: The genomes that need to get plotted
    :param colors: The colors uses, initiated by plotinit

    """
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



def plotlabels(ax, genes, nflips):
    """
    Finishes the plot, adding labels, titles and removing xticks
    """
    plt.ylabel("mutation (n)")
    plt.xlabel("genome sequence")
    plt.title("mutation sequence. nr of mutations = {}".format(nflips))
    plt.tick_params(
        axis='x',
        which='both',  # both major and minor ticks are affected
        bottom='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelbottom='off')  # labels along the bottom edge are off
    ax.axis([-0.05, len(genes[0]) / 4, -0.1, len(genes)])
    plt.show()

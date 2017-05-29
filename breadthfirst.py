"""
Helper functions for the breadth first algorithm
Leander
Nina

2017-5-16
"""


def traceMutations(archive, mut, genelen, geneOrigin, solution):
    """
    This function traces back the genomes, from starting genome to the solution.
    After only the mutation numbers were saved in a dictionary.

    input args:
        - archive: The dictionary which holds all the genomes that were found by doing mutations.
        - mut: 3 lists which hold the meaning of mutation indexes.
        - geneOrigin: The gene at which to stop searching. (One end of the search)(a list of numbers)
        - solution: The solution, which should be in the archive (Starting point of search)(a list of numbers)

    output:
        - genes: The genomes. A list of lists
        - mutationTracker: A mutationtracker! (list of mutation indexes)
        - costs: The saved cost of the sequences
        - levels: (A list with the depth-level of the genomes found by the search (should be sequential numbers))
    """

    # Start searching from solution
    key = ".".join(str(x) for x in solution)
    gene = solution
    if len(gene) > genelen:
        gene.pop()

    # Search untill geneOrigin is found
    geneOrigin = ".".join(str(x) for x in geneOrigin)

    genes = []
    mutationTrack = []
    costs = []
    mutsum = []
    mutsum2 = []
    levels = []

    while True:
        # Find mutation and gene sequence for this key, use information to go to the next

        level = archive[key][0]
        mutation = archive[key][1]

        genes.insert(0, gene[:])
        mutationTrack.insert(0, mutation)
        levels.insert(0, level)
        costs.insert(0, archive[key][2])
        mutsum.insert(0, archive[key][3])
        mutsum2.insert(0, archive[key][4])


        # Retrace the gene created by this mutation and use it as new key
        gene[mut.start[mutation]:mut.end[mutation]] = gene[mut.start[mutation]:mut.end[mutation]][::-1]
        key = ".".join(str(x) for x in gene)
        # print("key: {}".format(key))
        # print("mutation: {}".format(mutation))
        # print("level: {}".format(level))


        if key == geneOrigin:
            # Gene origin is found
            genes.insert(0, gene[:])
            costs.insert(0, archive[key][2])
            break

    return genes, mutationTrack, costs, mutsum, mutsum2, levels
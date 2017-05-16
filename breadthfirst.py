"""
Helper functions for the breadth first algorithm
Leander
Nina

2017-5-16
"""

def traceMutations(archive, mut, geneOrigin, solution):

    # Start searching from solution
    key = ".".join(str(x) for x in solution)
    gene = solution

    # Search untill geneOrigin is found
    geneOrigin = ".".join(str(x) for x in geneOrigin)

    genes = [solution[:]]
    mutationTrack = []
    levels = []

    while True:
        # Find mutation and gene sequence for this key, use information to go to the next
        level = archive[key][0]
        mutation = archive[key][1]

        # Retrace the gene created by this mutation and use it as new key
        gene[mut.start[mutation]:mut.end[mutation]] = gene[mut.start[mutation]:mut.end[mutation]][::-1]
        key = ".".join(str(x) for x in gene)

        genes.insert(0, gene[:])
        mutationTrack.insert(0, mutation)
        levels.insert(0, level)

        if key == geneOrigin:
            # Gene origin is found
            break

    return genes, mutationTrack, levels
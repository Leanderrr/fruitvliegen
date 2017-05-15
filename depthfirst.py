def new_branch(genes, mutationTrack):
    genes.pop()
    child = genes[-1][:]
    mutation = mutationTrack.pop() + 1
    return child, mutation
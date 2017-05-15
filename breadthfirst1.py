"""
First breadth first search algorithm to find a mutation sequence that turns one 'genome' into another

Leander
Nina

started: 2017-5-11
"""
from mutations import mutationlist


# geneOrigin = [4,3,2,1]
geneOrigin = [3,5,1,7,8,2,4,6] # test Genome that has to change to a sorted array
geneOrigin = [11, 6, 1, 2, 10, 7, 5, 8, 12, 13, 14, 15, 16, 17, 3, 4, 9]
geneLength = len(geneOrigin)
genes = []
genes.append(geneOrigin)
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

mutationTrack = [-1] # This keeps track of how many mutations have been tried for a child

# Create the list of possible mutations in this genome
mut = mutationlist(geneLength)

# Depth first search
archive = dict()
archive["".join(str(x) for x in geneOrigin)] = True
Go = True
maxDepth = 8
doubleCounter = 0

while Go:
    # stap 1: Kinderen maken
    child = genes[-1][:]
    # print("\n {}".format(genes))
    mutation = mutationTrack.pop() + 1

    while (mutation >= mut.max):
        # print("pruned because all mutation of this node have been tried {}".format(mutation))
        # Go up one level and continue with the other mutation
        genes.pop()
        mutation = mutationTrack.pop() + 1

        # print("going to do mutation {}".format(mutation))

    mutationTrack.append(mutation)  # mutation  kept track of

    # print("unaltered child {}\n".format(child))
    # print("\nmutation {}: section to flip: [{}]:[{}] = {} -> {}".format(mutation, mut.start[mutation], mut.end[mutation],
    #     child[mut.start[mutation]:mut.end[mutation]],  child[mut.start[mutation]:mut.end[mutation]][::-1]))

    # Stap 2: Mutate the child, according to the latest mutation of this 'node'
    child[mut.start[mutation]:mut.end[mutation]] = child[mut.start[mutation]:mut.end[mutation]][::-1]

    key = "".join(str(x) for x in child)

    if child == solution:
        # Stap 5: Controleren of een van de nieuwe kinderen de oplossing is
        Go = False
        print("\nWOHOOOOOO\n\n")
        genes.append(child[:])

    # stap 3: Controleren of het unieke kinnderen zijn
    elif (archive.get(key, False) != False) and (len(mutationTrack) > archive.get(key,100)): # Child already found
        # doubleCounter += 1
        # print("non-unique value encountered for #{} time".format(doubleCounter))
        print("mutationtracker: {}".format(mutationTrack))

    else:
        archive[key] = len(mutationTrack)

        if len(genes) > maxDepth:
            # Stoppen met tak als ie te diep wordt
            genes.pop()
            mutationTrack.pop()
            # print("pruned because of branch depth > {}".format(maxDepth))

        else:
            # Stap 7: Kinderen toevoegen aan stack, ze gaan ouders worden! Stap1
            genes.append(child[:])
            mutationTrack.append(-1)

print('final amount of double found sequences: {}'.format(doubleCounter))
#print("archive:\n")
#print(archive)
print("\ni,   start,  length, ending")
for i in range(len(mut.start)):
    print("[{0:<2}]: {1:<7} : {2:<7} : {3:<7}".format(i, mut.start[i]+1, mut.length[i], mut.end[i]))
print("number of possible mutations = {}\n".format(mut.max))

for gene in genes:
    print(gene)
print("final mutation tracker: {}".format(mutationTrack))
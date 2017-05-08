"""
First depth first search algorithm to find a mutation sequence that turns one 'genome' into another
Leander
Nina

started: 2017-5-2
"""

# geneOrigin = [4,3,2,1]
geneOrigin = [9, 8, 3, 1, 6, 7, 2, 4, 5] # test Genenome that has to change to a sorted array
geneLength = len(geneOrigin)
genes = []
genes.append(geneOrigin)
solution = [1,2,3,4,5,6,7,8,9]

mutationTrack = [-1] # This keeps track of how many mutations have been tried for a child

# Create the list of possible mutations in this genome
mutStart = []
mutLength = []
mutEnd = []
maxlength = geneLength-1
k = 1
while maxlength > 0:
    for j in range(maxlength):
        mutLength.append(k)
        mutStart.append(j)
        mutEnd.append(k + j + 1)
    k += 1
    maxlength -= 1
mutMax = len(mutLength) # Number of possible mutations

# Depth first search
archive = dict()
archive["".join(str(x) for x in geneOrigin)] = True
Go = True
maxDepth = 6
doubleCounter = 0


while Go:
    # stap 1: Kinderen maken
    child = genes[-1][:]
    print("\n {}".format(genes))
    mutation = mutationTrack.pop() + 1
    mutationTrack.append(mutation)  # mutation done and kept track of

    if (mutation >= mutMax):
        print("pruned because all mutations of this node have been tried")
        genes.pop()
        mutationTrack.pop()
        continue

    # print("unaltered child {}\n".format(child))
    print("\nmutation {}: section to flip: [{}]:[{}] = {} -> {}".format(mutation, mutStart[mutation], mutEnd[mutation],
        child[mutStart[mutation]:mutEnd[mutation]],  child[mutStart[mutation]:mutEnd[mutation]][::-1]))


    # Stap 2: Mutate the child, according to the latest mutation of this 'node'
    child[mutStart[mutation]:mutEnd[mutation]] = child[mutStart[mutation]:mutEnd[mutation]][::-1]
    #print(genes)
    print("mutationtracker: {}".format(mutationTrack))


    # Stap 5: Controleren of een van de nieuwe kinderen de oplossing is
    if child == solution:
        Go = False
        print("\nWOHOOOOOO\n\n")
        genes.append(child[:])
        break

    # stap 3: Controleren of het unieke kinnderen zijn
    key = "".join(str(x) for x in child)
    if archive.get(key, False)!= False: # Key in the archive
        doubleCounter += 1
        print("non-unique value encountered for #{} time".format(doubleCounter))
        continue


    # Stap 4: Kinderen die stap 4 overleeft hebben toevoegen aan archief
    archive[key] = True


    if len(genes) > maxDepth:
        # Stoppen met tak als ie te diep wordt
        genes.pop()
        mutationTrack.pop()
        print("pruned because of branch depth > {}".format(maxDepth))
    else:
        # Stap 7: Kinderen toevoegen aan stack, ze gaan ouders worden! Stap1
        genes.append(child[:])
        mutationTrack.append(-1)

print('final amount of double found sequences: {}'.format(doubleCounter))

#print("archive:\n")
#print(archive)
print("\ni,   start,  length, ending")
for i in range(len(mutStart)):
    print("[{0:<2}]: {1:<7} : {2:<7} : {3:<7}".format(i, mutStart[i]+1, mutLength[i], mutEnd[i]))
print("number of possible mutations = {}\n".format(mutMax))

for gene in genes:
    print(gene)
print("final mutation tracker: {}".format(mutationTrack))
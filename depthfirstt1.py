"""
First depth first search algorithm to find a agalwkng
Leander
Nina

2017-5-2
"""

geneOrigin = [1,3, 2, 6, 11, 9, 7, 4, 8, 5, 10]
# geneOrigin = [9, 8, 3 1, 6, 7, 2, 4, 5] # test Genenome that has to change to a sorted array
geneLength = len(geneOrigin)
genes = []
genes.append(geneOrigin)
solution = [1,2,3,4,5,6,7,8,9,10,11]

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
print(len(mutLength) - 1)
# Depth first search
Go = True
archive = dict()
archive["".join(str(x) for x in geneOrigin)] = True

maxDepth = 13
while Go:
    # stap 1: Kinderen maken
    child = genes[-1][:]

    mutation = mutationTrack.pop() + 1
    mutationTrack.append(mutation)  # mutation done and kept track of

    if (mutation >= len(mutLength)-1):
        # print("pruned because all mutations of this node have been tried")
        genes.pop()
        # print("Cutting tree at: {} because all options have been tried".format(mutationTrack))
        mutationTrack.pop()
        continue

    # print("unaltered child {}\n".format(child))
    #print("\nsection to flip: [{}]:[{}] = {} -> {}".format(mutStart[mutation], mutEnd[mutation],
    #    child[mutStart[mutation]:mutEnd[mutation]],  child[mutStart[mutation]:mutEnd[mutation]][::-1]))

    # Stap 2: Mutate the child, according to the latest mutation of this 'node'
    child[mutStart[mutation]:mutEnd[mutation]] = child[mutStart[mutation]:mutEnd[mutation]][::-1]
    #print(genes)
    #print("mutationtracker: {}".format(mutationTrack))

    # stap 3: Controleren of het unieke kinnderen zijn
    key = "".join(str(x) for x in child)
    if archive.get(key, False)!= False: # Key in the archive
        #print("gene {} found in archive already".format(child))
        continue


    # Stap 4 (voor later): Kinderen die stap 4 overleeft hebben toevoegen aan archief
    archive[key] = True

    # Stap 5: Controleren of een van de nieuwe kinderen de oplossing is
    if child == solution:
        Go = False
        print("\nWOHOOOOOO\n\n")
        genes.append(child[:])
        break

    if len(genes) > maxDepth:
        # Stoppen met tak als ie te diep wordt
        genes.pop()
        mutationTrack.pop()
        #print("pruned because of branch depth > {}".format(maxDepth))
    else:
        # Stap 7: Kinderen toevoegen aan stack, ze gaan ouders worden! Stap1
        genes.append(child[:])
        mutationTrack.append(-1)


#print("archive:\n")
#print(archive)
print("\ni,   start,  length, ending")
for i in range(len(mutStart)):
    print("[{0:<2}]: {1:<7} : {2:<7} : {3:<7}".format(i, mutStart[i]+1, mutLength[i], mutEnd[i]))
print("number of possible mutations = {}\n".format(len(mutLength)))

for gene in genes:
    print(gene)
print("final mutation tracker: {}".format(mutationTrack))
"""
First depth first search algorithm to find a mutation sequence that turns one 'genome' into another
MET ARCHIEF

Leander
Nina

started: 2017-5-2
"""

def main(geneOrigin =  [11, 8, 6, 4, 5, 2, 1, 3, 7, 9 ,10], maxDepth = 6, printer = True):
    from mutations import mutationlist
    import time

    # geneOrigin = [4,3,2,1]
    geneLength = len(geneOrigin)
    genes = []
    genes.append(geneOrigin)

    # Create solution array
    solution = []
    for i in range(1,geneLength+1):
        solution.append(i)

    mutationTrack = [-1] # This keeps track of how many mutations have been tried for a child

    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)

    # Depth first search
    archive = dict()
    archive["".join(str(x) for x in geneOrigin)] = True
    Go = True
    doubleCounter = 0
    tstart = time.time()
    while Go:
        # stap 1: Kinderen maken
        child = genes[-1][:]
        # print("\n {}".format(genes))
        mutation = mutationTrack.pop() + 1

        while (mutation >= mut.max):
            # print("pruned because all mutation of this node have been tried {}".format(mutation))
            # Go up one level and continue with the other mutation
            genes.pop()
            child = genes[-1][:]
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
            genes.append(child)

        # stap 3: Controleren of het unieke kinnderen zijn
        elif (archive.get(key, False) != False) and (len(mutationTrack) > archive.get(key,100)):
            # Child already found and this time it is at a later depth, so don't add this child to the stack
            doubleCounter += 1
            if doubleCounter % 100000 == 0:
                print(mutationTrack)
            # print("non-unique value encountered for #{} time".format(doubleCounter))

        else:
            archive[key] = len(mutationTrack)

            if len(genes) >= maxDepth:
                # Stoppen met tak als ie te diep wordt
                genes.pop()
                mutationTrack.pop()
                # print("pruned because of branch depth > {}".format(maxDepth))

            else:
                # Stap 7: Kinderen toevoegen aan stack, ze gaan ouders worden! Stap1
                genes.append(child)
                mutationTrack.append(-1)

    tduration = time.time() - tstart

    print('number of genomes in archive: {}'.format(len(archive)))
    print('# of double found sequences:  {}'.format(doubleCounter))
    #print("archive:\n")
    #print(archive)

    if printer == True:
        print("\ni,   start,  length, ending")
        for i in range(len(mut.start)):
            print("[{0:<2}]: {1:<7} : {2:<7} : {3:<7}".format(i, mut.start[i] + 1, mut.length[i], mut.end[i]))
        print("number of possible mutations = {}\n".format(mut.max))

        i = 0
        for gene in genes:
            print("{} {}".format(i, gene))
            i += 1



    print("final mutation tracker: {}".format(mutationTrack))
    print("program took {0:.3f} seconds to find solution".format(tduration))

if __name__ == '__main__':
    main()
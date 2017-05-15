"""
First breadth first search algorithm to find a mutation sequence that turns one 'genome' into another
MET ARCHIEF

Leander
Nina

started: 2017-5-15
"""

def main(geneOrigin =  [5,2,7,6,8,1,4,3], maxDepth = 4, printer = True):
    import sys
    import os 
    from mutations import mutationlist
    from Queue import Queue
    import time

    # geneOrigin = [4,3,2,1]
    geneLength = len(geneOrigin)
    genes = Queue()
    genes.put(geneOrigin)

    # Create solution array
    solution = []
    for i in range(1,geneLength+1):
        solution.append(i)

    mutationTrack = [-1] # This keeps track of how many mutations have been tried for a child
    # Create the list of possible mutations in this genome
    mut = mutationlist(geneLength)
    print(len(mut.start))
    # Breadth First Search
    archive = dict()
    archive["".join(str(x) for x in geneOrigin)] = True
    Go = True
    doubleCounter = 0
    tstart = time.time()
    level = 0

    while Go:

        # stap 1: Alle mogelijke kinderen maken en opslaan - checken of een van de kinderen de oplossing is. 
        level += 1
        mother = genes.get()

        #print(mother)

        # mutate the child - add to queu if not already in archive nor solution of the problem 
        for i in range (0, 27):     
            child = mother
            child[mut.start[i]:mut.end[i]] = child[mut.start[i]:mut.end[i]][::-1]
            #print(child)
            key = "".join(str(x) for x in child)

            # check if child is the solution
            if child == solution:
                Go = False
                print("wiehoe")
                print(level)
                genes.put(child)
                break
            # check if child is already in the archive - if so don't add this child to the queu
            elif (archive.get(key, False) != False):
                doubleCounter += 1

            # child is not the solution nor in archive - so should be added to the end of thequeu and archive
            else:
                genes.put(child)
                archive[key] = True
                #print("hallo")

    tduration = time.time() - tstart

    print('number of genomes in archive: {}'.format(len(archive)))
    print('# of double found sequences:  {}'.format(doubleCounter))
    #print("archive:\n")
    #print(archive)

    print("program took {0:.3f} seconds to find solution".format(tduration))

if __name__ == '__main__':
    main()
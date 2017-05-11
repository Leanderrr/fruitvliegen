""""
This will execute several of our methods to find a solution for a given gene
"""
import depthfirstt0
import depthfirstt1
import flipsorter
import random


testgenome = [1,2,3,4,5,6,7,8,9,10,11,12]
nTests = 10
printer = False
plot = False
maxdepthDesire = 5

# Test the programs nTest times with randomized sequences
for test in range(nTests):
    random.shuffle(testgenome)  # Randomize gene sequence
    # testgenome = [3, 5, 1, 6, 4, 2]

    print("\n\ntest: {}".format(test + 1))
    print("genome to convert: {}".format(testgenome))

    # Testing depthfirst 1, catching for indexError which occurs when no solution is found in the desired depth
    maxdepth = maxdepthDesire
    while True:
        try:
            print("Depthfirst 1 (with archive): ")
            depthfirstt1.main(testgenome, maxdepth, printer)
            break
        except IndexError: # Not deep enough
            maxdepth += 1
            print('TRY AGAIN: going to depth: {}'.format(maxdepth))

    # Testing depthfirst 0
    maxdepth = maxdepthDesire
    while True:
        try:
            print("\nDepthfirst 0 (no archive): ")
            depthfirstt0.main(testgenome, maxdepth, printer)
            break
        except IndexError: # Not deep enough
            maxdepth += 1
            print('TRY AGAIN: going to depth: {}'.format(maxdepth))

    # Testing the flipsorter
    print("\nFlipsorter: ")
    flipsorter.main(testgenome, plot, printer)



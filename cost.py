""""
Cost function used to decide priority in priority queue for BFS

Leander
Nina

2017-5-16
"""

def cost(function, padding, gene, mutsum=0, mutsum2=0, functionmut=False, mutation=0, mut=False, level=0):
    """
    input: function: Selection of which function should be used
           function2: Select
    """
    scoremut = 0
    scoreseq = 0

    # PADDING ON/OFF
    if padding == True:
        genome = gene[:]
        genome.extend([len(genome) + 1])
        genome.insert(0, 0)
    else:
        genome = gene[:]

    if mut != False:
        mutsum += mut.length[mutation]

        if functionmut == 1:
            scoremut = mutsum/10
        elif functionmut == 2:
            scoremut = mutsum/level
        elif functionmut == 3:
            scoremut = mutsum/level + (mut.length[mutation] * level)/5
            scoremut /= 15
        elif functionmut == 4:
            scoremut = mutsum2/level
            scoremut += 1 / 2 * pow(mut.length[mutation], 2)/5 + level/3
            scoremut /= 15
        elif functionmut == 5:
            scoremut = level/5

        mutsum2 += 1 / 2 * pow(mut.length[mutation], 2)

    # Cost function for genome sequences
    if function == 1:
        """
        Adds 1 to the score when a number is not adjacent to a number it should be adjacent to
        """
        for i in range (0, len(genome)-1):

            if genome[i] == genome[i+1]+1 or genome[i] == genome[i+1]-1:
                scoreseq += 0

            elif genome[i] != genome[i+1]+1 or genome[i] != genome[i+1]-1:
                scoreseq += 1


    elif function == 2:
        """
        Adds the difference between two adjacent numbers to the score
        """
        # calculate score
        for i in range(0, len(genome) - 1):
            scoreseq += abs(genome[i] - genome[i + 1])


    elif function == 3:
        """
        Look for sequentially correct numbers, add more to score every time it's correct
        """
        repeat = 1

        maxscore = sum(genome) - len(genome)
        # calculate score
        for i in range(0, len(genome) - 1):
            if abs(genome[i] - genome[i + 1]) == 1:
                scoreseq += repeat
                repeat += 1

            else:
                repeat = 1

        # converts score to priority
        scoreseq = maxscore / scoreseq


    elif function == 4:
        """
        Look for sequentially correct numbers, add more (with exponent) every time it's correct
        """
        repeat = 1
        maxscore = 0

        for i in range(1, len(genome)):

            maxscore += pow(i, 2)

            if abs(genome[i-1] - genome[i]) == 1:
                scoreseq += pow(repeat, 2)
                repeat += 1

            else:
               repeat = 1

        # converts score to priority
        scoreseq = maxscore / scoreseq


    elif function == 5:
        """
        Cost is calculated by adding the difference between all neighbours in the
        array to the power of 2, making numbers to be neighbouring numbers very
        far away from them very unlikely
        """
        for i in range(0, len(genome) - 1):
            scoreseq += pow(abs(genome[i] - genome[i + 1]), 2)


    elif function == 6:
        """
        Score calculated by counting the number of elements which are already sorted
        """
        repeat = 1
        maxscore = 0

        for i in range(0, len(genome) - 1):
            maxscore += pow((i+1),3)

            if genome[i] == genome[i + 1] + 1 or genome[i] == genome[i + 1] - 1:
                scoreseq += pow(repeat, 3)
                repeat += 1

            else:
                scoreseq += 0
                repeat = 1

        # converts score to priority
        scoreseq = maxscore / scoreseq

    elif function == 7:
        """
        looks how far off the gene is from its final desired position. It's really bad
        """

        for i in range(1, len(genome)):
            scoreseq += abs(genome[i] - i)

    if scoremut != 0:
        score = scoreseq + scoremut/2
    else:
        score = scoreseq

    return score, mutsum, mutsum2

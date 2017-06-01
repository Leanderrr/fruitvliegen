""""
Cost functions used to decide priority in priority queue for BEST FIRST

Leander
Nina

2017-5-16
"""

def cost(function, padding, gene, mutsum=0, mutsum2=0, functionmut=False,
         mutation=0, mut=False, level=0):

    """
    input:
    """
    # Padding on/off
    if padding == True:
        genome = addpadding(gene[:])
    else:
        genome = gene[:]

    # Call cost function for the mutation
    if mut != False:
        scoremut, mutsum, mutsum2 = mutationcost(functionmut,mutsum, mutsum2,
                                                 mut,mutation, level)

    else:
        scoremut = 0

    # Call Cost function for the genome sequence
    scoreseq = sequencecost(function, genome)

    score = scoreseq + scoremut

    return score, mutsum, mutsum2


def addpadding(gene):
    """
    Padding adds a 0 before the gene sequence , and a maximum+1 at the end.
    Causes the 1st and last gene in the genome to be in their place earlier.

    :param gene: the gene sequence that needs extra padding (a list)
    :return: genome: the gene sequence with extra padding
    """
    genome = gene[:]
    genome.extend([len(genome) + 1])
    genome.insert(0, 0)
    return genome


def mutationcost(functionmut, mutsum, mutsum2, mut, mutation, level):
    """
    Adds cost for mutation sizes

    :param functionmut: select which function will be executed
    :param scoremut: The current scoremut (0)
    :param mut: The object with meanings for mutation index
    :param level: which depth level the mutation has been done at
    :return: scoremut: The cost for the mutation
    :return: mutsum: mutationpoints as n
    :return: mutsum2: mutationpoints as 0.5*n^2
    """
    mutsum += mut.length[mutation]

    if functionmut == 1:
        scoremut = mutsum/20

    elif functionmut == 2:
        scoremut = mutsum/level

    elif functionmut == 3:
        """
        Score for mutation size n, taking into account previous mutations.
        Final scoremut value around 0 - 3
        """
        scoremut = mutsum/level + (mut.length[mutation] * level)/5
        scoremut /= 30

    elif functionmut == 4:
        """
        Score for mutation size 0.5*n^2, taking into account previous mutations
        """
        scoremut = mutsum2/level
        scoremut += 1 / 2 * pow(mut.length[mutation], 2)/5 + level/3
        scoremut /= 30

    elif functionmut == 5:
        scoremut = level/10

    mutsum2 += 1 / 2 * pow(mut.length[mutation], 2)

    return scoremut, mutsum, mutsum2


def sequencecost(function, genome):
    """
    Adds cost for how good the genome sequence is

    :param function: The function to execute
    :param genome: the genome to calculate cost for
    :return scoreseq: The cost of this genome sequence
    """
    scoreseq = 0
    if function == 1:
        """
        Adds 1 to the score when a number is not adjacent to a number
        it should be adjacent to
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
        Look for sequentially correct numbers, add more to score
        every time it's correct
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
        Look for sequentially correct numbers, add more (with exponent)
        every time it's correct
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
        Cost is calculated by adding the difference
        between all neighbours in the
        array to the power of 2
        """

        for i in range(0, len(genome) - 1):
            scoreseq += pow(abs(genome[i] - genome[i + 1]), 2)

    elif function == 6:
        """
        Score calculated by counting the number of elements
        which are already sorted
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

    return scoreseq

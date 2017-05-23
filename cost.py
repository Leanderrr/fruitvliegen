""""
Cost function used to decide priority in priority queue for BFS

Leander
Nina

2017-5-16
"""

def cost(function, function2, gene):
    """
    input: function: Selection of which function should be used
           function2: Select
    """
    score = 0

    # PADDING ON/OFF
    if function2 == True:
        genome = gene[:]
        genome.extend([len(genome) + 1])
        genome.insert(0, 0)
    else:
        genome = gene[:]

    # Cost function
    if function == 0:
        """

        """
        for i in range (0, len(genome)-1):

            if genome[i] == genome[i+1]+1 or genome[i] == genome[i+1]-1:
                score += 0

            elif genome[i] != genome[i+1]+1 or genome[i] != genome[i+1]-1:
                score += 1


    elif function == 1:
        """
        Adds 1 to the score when a number is not adjacent to a number it should be adjacent to
        """
        # calculate score
        for i in range(0, len(genome) - 1):
            score += abs(genome[i] - genome[i + 1])


    elif function == 2:
        """
        Look for sequentially correct numbers, add more to score every time it's correct
        """
        repeat = 1

        maxscore = sum(genome) - len(genome)
        # calculate score
        for i in range(0, len(genome) - 1):

            if genome[i] == genome[i + 1] + 1 or genome[i] == genome[i + 1] - 1:
                score += repeat
                repeat += 1

            else:
                score += 0
                repeat = 1

        # converts score to priority
        score = maxscore / score


    elif function == 3:
        """
        Look for sequentially correct numbers, add more (with exponent) every time it's correct
        """
        repeat = 1

        maxscore = sum(genome) - len(genome)
        for i in range(0, len(genome) - 1):

            if genome[i] == genome[i + 1] + 1 or genome[i] == genome[i + 1] - 1:
                score += pow(repeat, 2)
                repeat += 1

            else:
                score += 0
                repeat = 1

        # converts score to priority
        score = maxscore / score


    elif function == 4:
        """
        Cost is calculated by adding the difference between all neighbours in the
        array to the power of 2, making numbers to be neighbouring numbers very
        far away from them very unlikely
        """
        for i in range(0, len(genome) - 1):
            score += pow(abs(genome[i] - genome[i + 1]), 2)



    elif function == 5:
        """
        Score calculated by counting the number of elements which are already sorted
        """
        repeat = 1

        maxscore = sum(genome) - len(genome)
        for i in range(0, len(genome) - 1):

            if genome[i] == genome[i + 1] + 1 or genome[i] == genome[i + 1] - 1:
                score += pow(repeat, 3)
                repeat += 1

            else:
                score += 0
                repeat = 1

        # converts score to priority
        score = maxscore / score

    elif function == 6:
        """
        looks how far off the gene is from its final desired position. It's really bad
        """

        for i in range(1, len(genome)):
            score += abs(genome[i] - i)

    else:
        print("This score function does not exist (yet)/ incorrect function call. PLEASE STOP")
        return "ERROR"


    return score

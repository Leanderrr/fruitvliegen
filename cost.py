""""
Cost function used to decide priority in priority queue for BFS

Leander
Nina

2017-5-16
"""

def cost(function, gene):
    score = 0

    if function == 0:
        # Calculate priority
        for i in range (0, len(gene)-1):

            if gene[i] == gene[i+1]+1 or gene[i] == gene[i+1]-1:
                score += 0

            elif gene[i] != gene[i+1]+1 or gene[i] != gene[i+1]-1:
                score += 1


    elif function == 1:
        """
        Adds 1 to the score when a number is not adjacent to a number it should be adjacent to
        """
        # calculate score
        for i in range(0, len(gene) - 1):
            score += abs(gene[i] - gene[i + 1])


    elif function == 2:
        """
        Look for sequentially correct numbers, add more to score every time it's correct
        """
        repeat = 1

        maxscore = sum(gene) - len(gene)
        # calculate score
        for i in range(0, len(gene) - 1):

            if gene[i] == gene[i + 1] + 1 or gene[i] == gene[i + 1] - 1:
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

        maxscore = sum(gene) - len(gene)
        for i in range(0, len(gene) - 1):

            if gene[i] == gene[i + 1] + 1 or gene[i] == gene[i + 1] - 1:
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
        for i in range(0, len(gene) - 1):
            score += pow(abs(gene[i] - gene[i + 1]), 2)



    elif function == 5:
        """
        Score calculated by counting the number of elements which are already sorted
        """
        repeat = 1

        maxscore = sum(gene) - len(gene)
        for i in range(0, len(gene) - 1):

            if gene[i] == gene[i + 1] + 1 or gene[i] == gene[i + 1] - 1:
                score += pow(repeat, 3)
                repeat += 1

            else:
                score += 0
                repeat = 1

        # converts score to priority
        score = maxscore / score

    elif function == 6:
        """
        Look for sequentially correct numbers, add more more (with exponent) every time it's correct
        """

        for i in range(1, len(gene)):
            score += abs(gene[i]-i)


    elif function == 7:
        """

        """

    else:
        print("This score function does not exist (yet)/ incorrect function call")
        return "ERROR"

    return score

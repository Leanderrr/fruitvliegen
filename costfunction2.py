""""
Cost function used to decide priority in priority queue for BFS

Score calculated by counting the number of elements which are already
sorted

Nina

2017-5-17
"""
def main(gene):

    score = 0
    repeat = 1

    # calculate the maxscore
    maxscore = sum(gene) - len(gene)

    # calculate score
    for i in range (0, len(gene)-1):

        if gene[i] == gene[i + 1] + 1 or gene[i] == gene[i + 1] - 1:
            score += repeat
            repeat += 1

        else: #gene[i] != gene[i+1]+1 or gene[i] != gene[i+1]-1:
            score += 0
            repeat = 1

    # converts score to priority
    priority = maxscore / score

    return(priority)

if __name__ == "__main__":
    main()
""""
Cost function used to decide priority in priority queue for BFS

Score calculated by counting the number of elements which are already
sorted

Nina

2017-5-17
"""
def main(gene):

    #gene = [5,2,6,1,4,3,7,11,13,8,9,10]
    score = 0
    priority = 0
    repeat = 1

    # calculate the maxscore
    maxscore = sum(gene) - len(gene)
    print(maxscore)


    # calculate score
    for i in range (0, len(gene)-1):

        if gene[i] == gene[i + 1] + 1 or gene[i] == gene[i + 1] - 1:
            score += pow(repeat,2)
            repeat += 1

        else: #gene[i] != gene[i+1]+1 or gene[i] != gene[i+1]-1:
            score += 0
            repeat = 1

    # converts score to priority
    priority = maxscore / score

    return(priority)

if __name__ == "__main__":
    main()
""""
Cost function used to decide priority in priority queue for BFS

Cost calculated by adding the difference between all neighbours in the
array

Nina

2017-5-17
"""
def main(gene):

    score = 0

    # calculate score
    for i in range (0, len(gene)-1):
        score += abs(gene[i] - gene[i+1])

    print(score)
    return(score)

if __name__ == "__main__":
    main()
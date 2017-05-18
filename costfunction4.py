""""
Cost function used to decide priority in priority queue for BFS

Cost calculated by adding the difference between all neighbours in the
array to the power of 2, making numbers to be neighbouring numbers very 
far away from them very unlikely

Nina

2017-5-17
"""
def main(gene):

    score = 0

    # calculate score
    for i in range (0, len(gene)-1):
        score += pow(abs(gene[i] - gene[i+1]),2)

    # print(score)
    return(score)

if __name__ == "__main__":
    main()
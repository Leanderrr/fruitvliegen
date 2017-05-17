""""
Cost function used to decide priority in priority queue for BFS

Cost calculated by adding the difference between all neighbours in the
array

Nina

2017-5-17
"""
def main(gene):

    #gene = [5,2,6,1,4,3,7,11,13,8,9,10]
    # gene = [1,2,3,4,5,6,7,8,9,10,11]
    score = 0

    # calculate score
    for i in range (0, len(gene)-1):
        score += abs(gene[i+1] - gene[i])

    print(score)
    return(score)

if __name__ == "__main__":
    main()
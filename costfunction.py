""""
Cost function used to decide priority in priority queue for BFS

Function adds 1 to the score when a number is not adjacent to 
a number it should be adjacent to

Leander
Nina

2017-5-16
"""
def main(gene):

    #gene = [5,2,6,1,4,3,7,11,13,8,9,10]
    score = 0

    # Calculate priority
    for i in range (0, len(gene)-1):

        if gene[i] == gene[i+1]+1 or gene[i] == gene[i+1]-1:
            score += 0

        elif gene[i] != gene[i+1]+1 or gene[i] != gene[i+1]-1:
            score += 1

    return(score)

if __name__ == "__main__":
    main()
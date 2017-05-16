""""
Cost function used to decide priority in priority queue for BFS

Function adds 1 to the score when a number is not adjacent to 
a number it should be adjacent to

Leander
Nina

2017-5-16
"""
def main():

    testsequence = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
    score = 0

    # Calculate priority
    for i in range (0, len(testsequence)-1):

        if testsequence[i] == testsequence[i+1]+1 or testsequence[i] == testsequence[i+1]-1:
            score += 0

        elif testsequence[i] != testsequence[i+1]+1 or testsequence[i] != testsequence[i+1]-1:
            score += 1

    print("score = {}".format(score))
    return(score)

if __name__ == "__main__":
    main()
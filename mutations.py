class mutationlist:
    """

    :param geneLength: The length of a gene to calculate all possible mutations for
    :return: An object with several lists:
        .start = a list of on which gene each mutation starts
        .length = a list of how long those mutations are
        .end = a list of where these mutations end
        .max = the number of mutations possible for a gene sequence of geneLength length
    """

    def __init__(self, geneLength):
        self.start = []
        self.length = []
        self.end = []
        maxlength = geneLength - 1
        k = 1
        while maxlength > 0:
            for j in range(maxlength):
                self.length.append(k)
                self.start.append(j)
                self.end.append(k + j + 1)
            k += 1
            maxlength -= 1
            self.max = len(self.length)  # Number of possible mutations
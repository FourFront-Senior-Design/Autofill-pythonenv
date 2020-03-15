class Accuracy:
    def __init__(self, accessDb, autofill):
        self.autofill = autofill
        self.access = accessDb

    '''
    Calculates the accuracy using edit distance
    '''
    def levenshteinDistance(self, word1, word2):
        if word1 == None:
            word1 = ""
        if word2 == None:
            word2 = ""
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        distances = range(len(word1) + 1)
        for index2, char2 in enumerate(word2):
            newDistances = [index2 + 1]
            for index1, char1 in enumerate(word1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1 + 1],
                                                 newDistances[-1])))
            distances = newDistances
        return distances[-1]



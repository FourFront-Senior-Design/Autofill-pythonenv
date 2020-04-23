from AccuracyTests.accuracy import Accuracy

class RankAccuracy(Accuracy):
    rank = [ 'Rank', 'Rank2', 'Rank3', 'RankS_D', 'Rank2S_D', 'Rank3S_D', 'RankS_D_2', 'RankS_D_3', 'RankS_D_4']

    def __init__(self, access, autofill):
        super().__init__(access, autofill)


    def getRecordAcc(self, index):
        autofillRecord = self.autofill.getRecord(index)
        accessRecord = self.access.getRecord(index)

        filledPerRecord = 0
        missedPerRecord = 0
        incorrectPerRecord = 0
        avgPerRecord = 0
        for i in range(len(self.rank)):
            autofillRank = autofillRecord[self.rank[i]]
            accessRank = accessRecord[self.rank[i]]

            if autofillRank == None:
                autofillRank = ""

            if accessRank == None:
                accessRank = ""

            if autofillRank != "" and accessRank != "":
                diff = self.levenshteinDistance(autofillRank, accessRank)
                acc = (len(accessRank) - diff)/len(accessRank)
                avgPerRecord = avgPerRecord + acc
                filledPerRecord = filledPerRecord + 1

            if autofillRank == "" and accessRank != "":
                missedPerRecord = missedPerRecord + 1

            if autofillRank != "" and accessRank == "":
                incorrectPerRecord = incorrectPerRecord + 1

        if filledPerRecord != 0:
            avgPerRecord = avgPerRecord / filledPerRecord
        if (filledPerRecord + missedPerRecord + incorrectPerRecord) != 0:
            filledPerRecord = filledPerRecord / (filledPerRecord + missedPerRecord + incorrectPerRecord)
            incorrectPerRecord = incorrectPerRecord / (filledPerRecord + missedPerRecord + incorrectPerRecord)
            missedPerRecord = missedPerRecord / (filledPerRecord + missedPerRecord + incorrectPerRecord)
        return (avgPerRecord, missedPerRecord, filledPerRecord, incorrectPerRecord)

    def getAccuracy(self):
        numRecords = self.autofill.getNumRecords()
        avg = 0
        missed = 0
        filled = 0
        incorrect = 0

        for i in range(numRecords):
            (avgPerRecord, missedPerRecord, filledPerRecord, incorrectPerRecord) = self.getRecordAcc(i)
            avg = avg + avgPerRecord
            missed = missed + missedPerRecord
            filled = filled + filledPerRecord
            incorrect = incorrect + incorrectPerRecord

        avg = avg / numRecords
        missed = missed / numRecords
        filled = filled / numRecords
        incorrect = incorrect / numRecords

        return [avg, missed, filled, incorrect]

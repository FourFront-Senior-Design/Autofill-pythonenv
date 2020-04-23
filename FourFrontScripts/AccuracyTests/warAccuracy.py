from AccuracyTests.accuracy import Accuracy

class WarAccuracy(Accuracy):
    war = [ 'War', 'War2', 'War3', 'War4','WarS_D', 'War2S_D',
              'War3S_D', 'War4S_D', 'WarS_D_2', 'WarS_D_3', 'WarS_D_4']

    def __init__(self, access, autofill):
        super().__init__(access, autofill)


    def getRecordAcc(self, index):
        autofillRecord = self.autofill.getRecord(index)
        accessRecord = self.access.getRecord(index)

        filledPerRecord = 0
        missedPerRecord = 0
        incorrectPerRecord = 0
        avgPerRecord = 0
        for i in range(len(self.war)):
            autofillWar = autofillRecord[self.war[i]]
            accessWar = accessRecord[self.war[i]]

            if autofillWar == None:
                autofillWar = ""

            if accessWar == None:
                accessWar = ""

            if autofillWar != "" and accessWar != "":
                diff = self.levenshteinDistance(autofillWar, accessWar)
                acc = (len(accessWar) - diff)/len(accessWar)
                avgPerRecord = avgPerRecord + acc
                filledPerRecord = filledPerRecord + 1

            if autofillWar == "" and accessWar != "":
                missedPerRecord = missedPerRecord + 1

            if autofillWar != "" and accessWar == "":
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

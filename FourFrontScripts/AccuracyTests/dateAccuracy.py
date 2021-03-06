from AccuracyTests.accuracy import Accuracy

class DateAccuracy(Accuracy):
    birth = ['BirthDate', 'BirthDateS_D', 'BirthDateS_D_2', 'BirthDateS_D_3',
             'BirthDateS_D_4', 'BirthDateS_D_5', 'BirthDateS_D_6']

    death = ['DeathDate', 'DeathDateS_D', 'DeathDateS_D_2', 'DeathDateS_D_3',
             'DeathDateS_D_4', 'DeathDateS_D_5', 'DeathDateS_D_6']

    def __init__(self, access, autofill):
        super().__init__(access, autofill)


    def getRecordAcc(self, index, array):
        autofillRecord = self.autofill.getRecord(index)
        accessRecord = self.access.getRecord(index)

        filledPerRecord = 0
        missedPerRecord = 0
        incorrectPerRecord = 0
        avgPerRecord = 0
        for i in range(len(array)):
            autofillDate = autofillRecord[array[i]]
            accessDate = accessRecord[array[i]]

            if autofillDate == None:
                autofillDate = ""

            if accessDate == None:
                accessDate = ""

            if autofillDate != "" and accessDate != "":
                diff = self.levenshteinDistance(autofillDate, accessDate)
                acc = (len(accessDate) - diff)/len(accessDate)
                if acc < 0:
                    print("neg")
                avgPerRecord = avgPerRecord + acc
                filledPerRecord = filledPerRecord + 1

            if autofillDate == "" and accessDate != "":
                missedPerRecord = missedPerRecord + 1

            if autofillDate != "" and accessDate == "":
                incorrectPerRecord = incorrectPerRecord + 1

        if filledPerRecord != 0:
            avgPerRecord = avgPerRecord / filledPerRecord
        if (filledPerRecord + missedPerRecord + incorrectPerRecord) != 0:
            filledPerRecord = filledPerRecord / (filledPerRecord + missedPerRecord + incorrectPerRecord)
            incorrectPerRecord = incorrectPerRecord / (filledPerRecord + missedPerRecord + incorrectPerRecord)
            missedPerRecord = missedPerRecord / (filledPerRecord + missedPerRecord + incorrectPerRecord)
        return (avgPerRecord, missedPerRecord, filledPerRecord, incorrectPerRecord)

    def getAccuracy(self, array):
        numRecords = self.autofill.getNumRecords()
        avg = 0
        missed = 0
        filled = 0
        incorrect = 0
        print(numRecords)

        for i in range(numRecords):
            (avgPerRecord, missedPerRecord, filledPerRecord, incorrectPerRecord) = self.getRecordAcc(i, array)
            if avgPerRecord > 1:
                print("Data: ", avgPerRecord)
            avg = avg + avgPerRecord
            missed = missed + missedPerRecord
            filled = filled + filledPerRecord
            incorrect = incorrect + incorrectPerRecord

        avg = avg / numRecords
        missed = missed / numRecords
        filled = filled / numRecords
        incorrect = incorrect / numRecords

        return [avg, missed, filled, incorrect]

    def getBirthDateAcc(self):
        return self.getAccuracy(self.birth)

    def getDeathDateAcc(self):
        return self.getAccuracy(self.death)

from AccuracyTesting.accuracy import Accuracy

class MarkerAccuracy(Accuracy):
    dkl = ['MarkerType']

    def __init__(self, access, autofill):
        super().__init__(access, autofill)

    def getDateAccuracy(self, index):
        autofillRecord = self.autofill.getRecord(index)
        accessRecord = self.access.getRecord(index)
        averageDiff = 0
        countDiff = 0
        incorrect = 0
        missing = 0
        for i in range(len(self.dkl)):
            autofillMarker = autofillRecord[self.dkl[i]]
            accessMarker = accessRecord[self.dkl[i]]

            if autofillMarker != "" and accessMarker != "":
                diff = self.levenshteinDistance(autofillMarker, accessMarker)
                if diff != 0:
                    print("Filled, but incorrect: ", autofillMarker, accessMarker, diff)
                averageDiff += diff
                countDiff = countDiff + 1

            if accessMarker == "" and autofillMarker != "":
                incorrect = incorrect + 1
            if accessMarker != "" and autofillMarker == "":
                missing = missing + 1
            if countDiff != 0:
                averageDiff = averageDiff / countDiff
        return (averageDiff, incorrect, missing)

    def getAccuracy(self):
        size = self.autofill.getNumRecords()
        averageDateAccuracy = 0
        totalMissingDate = 0
        totalIncorrectDate = 0
        for i in range(size):
            (averageDateDiff, incorrectDate, missingDate) = self.getDateAccuracy(i)
            averageDateAccuracy += averageDateDiff
            totalMissingDate += missingDate
            totalIncorrectDate += incorrectDate
        averageDateAccuracy = averageDateAccuracy / size
        print("Average Date Diff: ", averageDateAccuracy)
        print("Total Missing Dates: ", totalMissingDate)
        print("Total Incorrect Dates: ", totalIncorrectDate)

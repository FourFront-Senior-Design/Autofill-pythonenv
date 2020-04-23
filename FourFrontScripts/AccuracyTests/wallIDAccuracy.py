from AccuracyTests.accuracy import Accuracy

class WallIDAccuracy(Accuracy):

    def __init__(self, access, autofill):
        super().__init__(access, autofill)

    def getRecordAcc(self, index):
        accessRecord = self.access.getRecord(index)
        filledPerRecord = 0
        missedPerRecord = 0
        avgPerRecord = 0
        incorrectPerRecord = 0

        autofillWallID = "0"
        accessWallID = accessRecord['Wall']

        if autofillWallID == None:
            autofillWallID = ""

        if accessWallID == None:
            accessWallID = ""

        if autofillWallID != "" and accessWallID != "":
            diff = self.levenshteinDistance(autofillWallID, accessWallID)
            avgPerRecord = (len(accessWallID) - diff) / len(accessWallID)
            filledPerRecord = 1

        if accessWallID != "" and autofillWallID == "":
            missedPerRecord = 1

        if accessWallID == "" and autofillWallID != "":
            incorrectPerRecord = 1

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

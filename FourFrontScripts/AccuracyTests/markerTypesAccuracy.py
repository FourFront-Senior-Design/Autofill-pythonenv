from AccuracyTests.accuracy import Accuracy

class MarkerAccuracy(Accuracy):

    def __init__(self, access, autofill):
        super().__init__(access, autofill)

    def getRecordAcc(self, index):
        autofillRecord = self.autofill.getRecord(index)
        accessRecord = self.access.getRecord(index)
        filledPerRecord = 0
        missedPerRecord = 0
        avgPerRecord = 0
        incorrectPerRecord = 0

        autofillMarker = autofillRecord['MarkerType']
        accessMarker = accessRecord['MarkerType']

        if autofillMarker == None:
            autofillMarker = ""

        if accessMarker == None:
            accessMarker = ""

        if autofillMarker != "" and accessMarker != "":
            diff = self.levenshteinDistance(autofillMarker, accessMarker)
            avgPerRecord = (len(accessMarker) - diff) / len(accessMarker)
            filledPerRecord = 1

        if accessMarker != "" and autofillMarker == "":
            missedPerRecord = 1

        if accessMarker == "" and autofillMarker != "":
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

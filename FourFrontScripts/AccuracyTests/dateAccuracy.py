from AccuracyTests.accuracy import Accuracy

class DateAccuracy(Accuracy):
    dkl = ['BirthDate', 'DeathDate', 'BirthDateS_D', 'DeathDateS_D',
       'BirthDateS_D_2', 'DeathDateS_D_2', 'BirthDateS_D_3', 'DeathDateS_D_3',
       'BirthDateS_D_4', 'DeathDateS_D_4', 'BirthDateS_D_5', 'DeathDateS_D_5',
       'BirthDateS_D_6', 'DeathDateS_D_6']

    def __init__(self, access, autofill):
        super().__init__(access, autofill)

    def getDateAccuracy(self, index):
        autofillRecord = self.autofill.getRecord(index)
        accessRecord = self.access.getRecord(index)
        averageDiff = {}
        incorrect = {}
        missing = {}
        perfect = {}
        for i in range(len(self.dkl)):
            autofillDate = autofillRecord[self.dkl[i]]
            accessDbDate = accessRecord[self.dkl[i]]

            if autofillDate == None:
                autofillDate = ""

            if accessDbDate == None:
                accessDbDate = ""

            per = 0
            avgDiff = 0
            wrong = 0
            miss = 0
            if autofillDate != "" and accessDbDate != "":
                diff = self.levenshteinDistance(autofillDate, accessDbDate) / max(len(accessDbDate), len(autofillDate))
                if diff == 0:
                    per = per + 1
                else:
                    avgDiff += diff

            if accessDbDate == "" and autofillDate != "":
                wrong = wrong + 1
            if accessDbDate != "" and autofillDate == "":
                miss = miss + 1

            averageDiff[self.dkl[i]] = avgDiff
            perfect[self.dkl[i]] = per
            incorrect[self.dkl[i]] = wrong
            missing[self.dkl[i]] = miss

        return (averageDiff, perfect, incorrect, missing)

    def getAccuracy(self):
        size = self.autofill.getNumRecords()
        averageDateAccuracy = {}
        totalMissingDate = {}
        totalPerfect = {}
        totalIncorrectDate = {}

        cntNonZeroDiff = 0;
        for i in range(len(self.dkl)):
            averageDateAccuracy[self.dkl[i]] = 0
            totalMissingDate[self.dkl[i]] = 0
            totalPerfect[self.dkl[i]] = 0
            totalIncorrectDate[self.dkl[i]] = 0

        for i in range(size):
            (averageDateDiff, perfect, incorrectDate, missingDate) = self.getDateAccuracy(i)
          #  print(averageDateDiff)
            for j in range(len(self.dkl)):
                averageDateAccuracy[self.dkl[j]] += averageDateDiff[self.dkl[j]]
                if averageDateDiff[self.dkl[j]] != 0:
                    cntNonZeroDiff = cntNonZeroDiff + 1
                totalMissingDate[self.dkl[j]] += missingDate[self.dkl[j]]
                totalIncorrectDate[self.dkl[j]] += incorrectDate[self.dkl[j]]
                totalPerfect[self.dkl[j]] += perfect[self.dkl[j]]

        for j in range(len(self.dkl)):
            averageDateAccuracy[self.dkl[j]] = averageDateAccuracy[self.dkl[j]] / cntNonZeroDiff * 10
            totalMissingDate[self.dkl[j]] = totalMissingDate[self.dkl[j]] / size * 100
            totalIncorrectDate[self.dkl[j]] = totalIncorrectDate[self.dkl[j]] / size * 100
            totalPerfect[self.dkl[j]] = totalPerfect[self.dkl[j]] / size * 100

        return [averageDateAccuracy, totalPerfect, totalIncorrectDate, totalMissingDate]

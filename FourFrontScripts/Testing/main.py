from Testing.AccessDatabase import AccessDatabase
from Testing.AutofillData import AutofillData
from Testing.dateAccuracy import DateAccuracy
from Testing.markerTypesAccuracy import MarkerAccuracy
import csv

section = r"\\athos.cse.sdsmt.edu\FourFront\opy2\OPY2\15.2238.061 Ft. Richardson National Cemetery\Data\Section000FF"
database = r"\FRNC_SectionFF_be.accdb"
tempFiles = r"\tempFiles"
accessDb = AccessDatabase(section + database)
autofill = AutofillData(section + tempFiles)

filename = "C:/Python/FourFrontScripts/accuracyResults.csv"

with open(filename, 'a') as csvfile:
    ## Date Accuracy
    date = DateAccuracy(accessDb, autofill)
    [averageDateAccuracy, totalPerfect, totalIncorrectDate, totalMissingDate] = date.getAccuracy()

    columns = list(averageDateAccuracy.keys())
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows([averageDateAccuracy, totalPerfect, totalIncorrectDate, totalMissingDate])
## MarkerType Accuracy
#marker = MarkerAccuracy(accessDb, autofill)
#marker.getAccuracy()
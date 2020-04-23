from DataAccess.Database import AccessDatabase
from DataAccess.TempFileData import TempFileData
from AccuracyTests.dateAccuracy import DateAccuracy
from AccuracyTests.markerTypesAccuracy import MarkerAccuracy
from AccuracyTests.warAccuracy import WarAccuracy
from AccuracyTests.wallIDAccuracy import WallIDAccuracy
from AccuracyTests.rankAccuracy import RankAccuracy
import csv

section = r"" #Add path to the section folder here
database = [f for f in os.listdir(section) if f.endswith('_be.accdb')][0]
tempFiles = r"\tempFiles"
accessDb = AccessDatabase(section + "\\" + database)
autofill = TempFileData(section + tempFiles)

filename = r"C:\Python\FourFrontScripts\AccuracyTests\AccuracyResults" + database.split('.')[0] + ".txt"

file = open(filename,"w")

wallId = WallIDAccuracy(accessDb, autofill)
wallAcc = wallId.getAccuracy()

#marker = MarkerAccuracy(accessDb, autofill)
#markerAcc = marker.getAccuracy()

dates = DateAccuracy(accessDb, autofill)
birth = dates.getBirthDateAcc()
death = dates.getDeathDateAcc()

war = WarAccuracy(accessDb, autofill)
warAcc = war.getAccuracy()

rank = RankAccuracy(accessDb, autofill)
rankAcc = rank.getAccuracy()

file.write("Accuracy, Missing, Filled, Incorrect\n")
#file.writelines("Marker Type: " + str(markerAcc) + "\n")
file.writelines("Wall ID: " + str(wallAcc)+ "\n")
file.writelines("Birth Date: " + str(birth)+ "\n")
file.writelines("Death Date: " + str(death)+ "\n")
file.writelines("War: " + str(warAcc)+ "\n")
file.writelines("Ranks: " + str(rankAcc)+ "\n")
file.close()

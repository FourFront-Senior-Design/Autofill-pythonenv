from DataAccess.Database import AccessDatabase
from DataAccess.OCRData import OCRData
from DataPreparation.BestMatch import BestMatch
import csv

#Name of the section
section = r""
#Names of the backend database in this section
database = r"\.accdb"
googleVision =  r"\GoogleVisionData"
filename = "C:/Python/FourFrontScripts/TestData/data.csv"

#Connects to the MS Access Database
accessDb = AccessDatabase(section + database)

with open(filename, 'a', newline='') as csvfile:
   # columns = ["word", "markerType", "ImageLocation", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "category"]
    writer = csv.writer(csvfile)
   # writer.writerow(columns)

    for i in range(accessDb.getNumRecords()):
        record = accessDb.getRecord(i)

        #Connects to the OCR data associated with the images in the record
        frontImageOCR = section + googleVision + "\\" + record['ImageHyperlink_Front'].split('\\')[1].split('.')[0]+'.json'
        backImageOCR = ""
        if record['ImageHyperlink_Back'] != None:
            backImageOCR = section + googleVision + "\\" + record['ImageHyperlink_Back'].split('\\')[1].split('.')[0]+'.json'
        ocrData = OCRData(frontImageOCR, backImageOCR)

        '''
        Gets all the words from the ocr and access database
        '''
        ocrPerson = ocrData.getWordList()
        accessPerson = accessDb.getFilledPersonData(i)

        '''
        Creates the best match
        '''
        best = BestMatch(ocrPerson, accessPerson)
        access_ocr = best.create()

        '''
        Labels the ocr database by checking in which column
        the closest matching word belongs in
        '''
        labeledOCR = []
        for item in access_ocr:
            if item[0] == '': continue
            inAccessDb = item[0]
            label = accessDb.getColumnName(i, inAccessDb)
            labeledOCR.append([item[1], label])

        '''
        Writes the data of the word in the database in the format:
        ["word", "markerType", "ImageLocation", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "category"]
        '''
        for item in labeledOCR:
            coordinates, location = ocrData.getCoordinatesLocation(item[0])
            if coordinates != []:
                x1, y1 = coordinates[0]['x'], coordinates[0]['y']
                x2, y2 = coordinates[1]['x'], coordinates[1]['y']
                x3, y3 = coordinates[2]['x'], coordinates[2]['y']
                x4, y4 = coordinates[3]['x'], coordinates[3]['y']
                row = [item[0], accessDb.getMarkerType(i), location, x1, y1, x2, y2, x3, y3, x4, y4, item[1]]
                writer.writerow(row)

from DataPrep.AccessDatabase import AccessDatabase
from DataPrep.OCR import OCRData
from DataPrep.BestMatch import BestMatch
import csv

section = r"C:\Users\7405148\Desktop\Sha\2020_Spring\Senior_Design_II\categorization\TestDatabases\SectionC-10_FlatMarkerTypes"
database = r"\SJVNC_SectionC-10_be.accdb"
googleVision =  r"\GoogleVisionData"
filename = "C:/Python/FourFrontScripts/DataPrep/data.csv"
accessDb = AccessDatabase(section + database)

with open(filename, 'a', newline='') as csvfile:
    #columns = ["word", "markerType", "ImageLocation", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "category"]
    writer = csv.writer(csvfile)
    #writer.writerow(columns)

    for i in range(accessDb.getNumRecords()):
        record = accessDb.getRecord(i)
        frontImageOCR = section + googleVision + "\\" + record['ImageHyperlink_Front'].split('\\')[1].split('.')[0]+'.json'
        backImageOCR = ""
        if record['ImageHyperlink_Back'] != None:
            backImageOCR = section + googleVision + "\\" + record['ImageHyperlink_Back'].split('\\')[1].split('.')[0]+'.json'
        ocrData = OCRData(frontImageOCR, backImageOCR)
        ocrPerson = ocrData.getWordList()
        accessPerson = accessDb.getFilledPersonData(i)

        best = BestMatch(ocrPerson, accessPerson)
        access_ocr = best.create()

        labeledOCR = []
        for item in access_ocr:
            if item[0] == '': continue
            inAccessDb = item[0]
            label = accessDb.getColumnName(inAccessDb)
            labeledOCR.append([item[1], label])

        #print(labeledOCR)

        c = 0
        for item in labeledOCR:
            coordinates, location = ocrData.getCoordinatesLocation(item[0])
            if coordinates != []:
                c = c+1
                x1, y1 = coordinates[0]['x'], coordinates[0]['y']
                x2, y2 = coordinates[1]['x'], coordinates[1]['y']
                x3, y3 = coordinates[2]['x'], coordinates[2]['y']
                x4, y4 = coordinates[3]['x'], coordinates[3]['y']
                row = [item[0], accessDb.getMarkerType(i), location, x1, y1, x2, y2, x3, y3, x4, y4, item[1]]
                writer.writerow(row)
        print(c, len(labeledOCR))



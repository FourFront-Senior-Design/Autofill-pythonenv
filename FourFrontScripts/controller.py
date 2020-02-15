import os
import sys
import googleVisionOCR
import dateExtraction
import rankExtraction
import dataTemplate
import json

from os import listdir, mkdir
from os.path import isfile, join
from copy import deepcopy

def main(argv):
    filePath = sys.argv[1]
    #uprightFlatTypeList = sys.argv[2]

    googleVisionOCR.OCR(filePath)
    
    jsonPath = filePath + "\\GoogleVisionData\\"
    tempPath = filePath + "\\tempFiles\\"
    if not os.path.isdir(tempPath):
        os.mkdir(tempPath)

    emptyData = dataTemplate.data_template
    
    # Do we need to sort fileList?
    fileList = [f for f in listdir(jsonPath) if isfile(join(jsonPath, f))]
    for f in fileList:
        recordData = deepcopy(emptyData)
        
        currentFilePath = filePath + "\\GoogleVisionData\\" + f
        
        with open(currentFilePath, 'r') as file:
            try:
                jsonData = json.load(file)
            except:
                pass
        
        dates = dateExtraction.extractDates(currentFilePath, jsonData)
                
        for d in dates:
            recordData[d] = dates[d]
            
        #ranks = rankExtraction.extractRanks(currentFilePath, jsonData)
        
        #for r in ranks:
        #    recordData[r] = ranks[r]
        
        # Add autofill modules here

        outputFilePath = tempPath + f.split(".")[0] + ".tmp"
        
        file = open(outputFilePath, "w+")
        
        file.write("")
        
        for i in recordData:
            file.write(i + ":" + recordData[i] + "\n")

        file.close()
                    
if __name__ == "__main__":
    main(sys.argv)

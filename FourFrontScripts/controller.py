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

    googleVisionOCR.OCR(filePath)
    
    jsonPath = filePath + "\\GoogleVisionData\\"
    tempPath = filePath + "\\tempFiles\\"
    if not os.path.isdir(tempPath):
        os.mkdir(tempPath)

    emptyData = dataTemplate.data_template
    
    # Open "recordTypeList.tmp" file and read into list, strip at ends
    recordTypeList = []
    with open(tempPath + "\\recordTypeList.tmp", 'r') as file:
        recordTypeList = file.readlines()
    recordTypeList = [line.strip() for line in recordTypeList]
    # recordTypeList is now a list containing the arguments to be sent to each
    # extraction module/script

    for line in recordTypeList:
        recordData = deepcopy(emptyData)

        # set up file path/names
        filePath1 = filePath2 = ""
        fileList = line.split()

        # set up arguments (file path/names)
        argList = []
        if len(fileList) == 1:
            filePath1 = jsonPath + fileList[0] + ".json"
            argList.append(filePath1)
        if len(fileList) == 2:
            filePath1 = jsonPath + fileList[0] + ".json"
            argList.append(filePath1)
            filePath2 = jsonPath + fileList[1] + ".json"
            argList.append(filePath2)
        
        # pass argList to extraction modules
        args = ""
        if len(argList) == 1:
            args = argList[0]
        elif len(argList) == 2:
            args = argList[0] + " " + argList[1]

        # call extraction modules
        dates = dateExtraction.extractDates(args)
        # add more calls to extraction modules here

        # fill recordData
        for d in dates:
            recordData[d] = dates[d]
        # add more extraction fill loops here


        # write output recordData to .tmp files 
        outputFilePath = tempPath + fileList[0] + ".tmp"
        
        file = open(outputFilePath, "w+")
        
        file.write("")
        
        for i in recordData:
            file.write(i + ":" + recordData[i] + "\n")
    
        file.close()
                    
if __name__ == "__main__":
    main(sys.argv)

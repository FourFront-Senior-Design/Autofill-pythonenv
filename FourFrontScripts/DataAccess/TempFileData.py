# Reads the temp files with the extracted texts in the section

import os

class TempFileData:
    '''
    Reads all the temp files in the given location
    Each temp file data is a dictionary
    '''
    def __init__(self, tempFilesPath):
        self.__path = tempFilesPath
        self.__records = []
        for filename in os.listdir(self.__path):
            if filename.endswith(".tmp"):
                with open(self.__path + "\\"+filename) as f:
                    d = dict()
                    for line in f:
                        (key, val) = line.split(":")
                        d[key.strip()] = val.strip()
                self.__records.append(d)

    def getRecord(self, i):
        return self.__records[i]

    def getNumRecords(self):
        return len(self.__records)

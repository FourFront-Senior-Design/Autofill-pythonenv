import os

class AutofillData:

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

#auto = AutofillData(r"C:\Users\7405148\Desktop\Sha\2020 Spring\Senior Design II\categorization\TestDatabases\Section0000P_UprightMakerTypes\tempFiles")
#print(auto.getNumRecords())
#print(auto.getRecord(2)["BirthDate"])




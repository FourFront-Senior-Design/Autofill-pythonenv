# Database access

import pyodbc
from DataStructures import dataTemplate

class AccessDatabase:

    def __init__(self, databasePath):
        self._conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=%s' % databasePath
            )
        self._conn = pyodbc.connect(self._conn_str)
        self._cursor = self._conn.cursor()
        self._cursor.execute('select * from master')
        columns = [column[0] for column in self._cursor.description]
        self._record = []
        for row in self._cursor.fetchall():
            self._record.append(dict(zip(columns, row)))
        self.columnPerWord = []

    def getRecord(self, i):
        return self._record[i]

    def getNumRecords(self):
        return len(self._record)

    def getMarkerType(self, i):
        return self._record[i]['MarkerType']

    '''
    Gets the words in the person object in the record
    
    Depending on the number of words in each column it 
    creates the columnPerWord array that will be used to
    get the column in which the word belongs to in the
    getColumnNames function
    '''
    def getFilledPersonData(self, i):
        data = self._record[i]
        keys = dataTemplate.data_template.keys()
        filledPerson = []
        for x in keys:
            if x == 'GravesiteNumber' or x == 'MarkerType' \
                or x == 'Emblem1' or x == 'Emblem2': continue
            if data[x] == None or data[x] == '': continue
            val = str(data[x])
            if ' ' in val:
                words = val.split()
                self.columnPerWord.extend([x]*len(words))
                filledPerson.extend(words)
            elif '/' in val:
                nums = val.split('/')
                nums = [y.lstrip('0') for y in nums]
                self.columnPerWord.extend([x]*len(nums))
                filledPerson.extend(nums)
            else:
                self.columnPerWord.append(x)
                filledPerson.append(val)
        return filledPerson

    '''
    Gets the column in which the word exists
    '''
    def getColumnName(self, i, word):
        col = -1
        data = self.getRecord(i)
        for i in range(len(self.columnPerWord)):
            columnName = self.columnPerWord[i]
            if data[columnName] == None: continue
            if word in str(data[columnName]):
                col = i
                break
        if col != -1:
            name = self.columnPerWord[col]
            self.columnPerWord.remove(name)
            return name
        return ''

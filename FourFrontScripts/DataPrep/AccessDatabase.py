import pyodbc
import dataTemplate

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
        self.template = dataTemplate.data_template
        self.columnPerWord = []

    def getRecord(self, i):
        return self._record[i]

    def getFilledPersonData(self, i):
        data = self._record[i]
        for key in self.template.keys():
            self.template[key] = data[key]
        if 'GravesiteNumber' in self.template.keys():
            del self.template['GravesiteNumber']
        if 'MarkerType' in self.template.keys():
            del self.template['MarkerType']
        if 'Emblem1' in self.template.keys():
            del self.template['Emblem1']
        if 'Emblem2' in self.template.keys():
            del self.template['Emblem2']

        filledPerson = []
        for x in self.template.keys():
            if self.template[x] == None or self.template[x] == '': continue
            val = self.template[x]
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


    def getNumRecords(self):
        return len(self._record)

    def getColumnName(self, word):
        col = -1
        for i in range(len(self.columnPerWord)):
            columnName = self.columnPerWord[i]
            if self.template[columnName] == None: continue
            if word in self.template[columnName]:
                col = i
                break
        if col != -1:
            name = self.columnPerWord[col]
            self.columnPerWord.remove(name)
            return name
        return ''

    def getTemplate(self):
        val = dict()
        for x in self.template:
            if self.template[x] == None or self.template[x] == '': continue
            val[x] = self.template[x]
        return self.template

    def getMarkerType(self, i):
        return self._record[i]['MarkerType']
#databasePath = r"C:\Users\7405148\Desktop\Sha\2020_Spring\Senior_Design_II\categorization\TestDatabases\Section0000P_UprightMakerTypes\FRNC_SectionP_be.accdb"
#access = AccessDatabase(databasePath)
#print(access.getFilledPersonData(1))

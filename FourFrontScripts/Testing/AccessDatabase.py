import pyodbc

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

    def getRecord(self, i):
        return self._record[i]

    def getNumRecords(self):
        return len(self._record)

#databasePath = r"C:\Users\7405148\Desktop\Sha\2020_Spring\Senior_Design_II\categorization\TestDatabases\Section0000P_UprightMakerTypes\FRNC_SectionP_be.accdb"
#access = AccessDatabase(databasePath)
#print(access.getRecord(2))

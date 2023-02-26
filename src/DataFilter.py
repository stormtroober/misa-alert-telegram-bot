from Resources import NoPrintCode
import MessageFormatter
from Settings import global_treshold_level
import sqlite3


# sql = '''CREATE TABLE MisaLevels(station, value, timestamp)'''



class DataFilter:
    def __init__(self):
        self.global_treshold_level = global_treshold_level
        self.con = sqlite3.connect("Records.db")
        self.cur = self.con.cursor()
        self.insertSqlStatement = '''INSERT INTO MisaLevels (station, value, timestamp) VALUES (?, ?, ?)'''

    def changeTreshold(self, value):
        self.global_treshold_level = value
    
    def filter(self,stationsData):
        IsOverTreshold = False
        for sd in stationsData:
            data = (str(sd['code']) + ' - ' + sd['stationPlace'], sd['value'], sd['lastUpdateTime'])
            print(data)
            self.cur.execute(self.insertSqlStatement, data)
            self.con.commit()
            if float(sd['value']) >= self.global_treshold_level:
                IsOverTreshold = True

        if IsOverTreshold:
            return MessageFormatter.formatStationsMessage(stationsData)
        else:
            return MessageFormatter.formatStationsMessage(NoPrintCode)
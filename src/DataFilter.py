from Resources import NoPrintCode
import MessageFormatter
from Settings import global_treshold_level
  
class DataFilter:
    def __init__(self):
        self.global_treshold_level = global_treshold_level

    def changeTreshold(self, value):
        self.global_treshold_level = value
    
    def filter(self,stationsData):
        IsOverTreshold = False
        for sd in stationsData:
            if float(sd['value']) >= self.global_treshold_level:
                IsOverTreshold = True

        if IsOverTreshold:
            return MessageFormatter.formatStationsMessage(stationsData)
        else:
            return MessageFormatter.formatStationsMessage(NoPrintCode)
from Settings import global_treshold_level
from Resources import NoPrintCode
import MessageFormatter

def filter(stationsData):
    IsOverTreshold = False
    for sd in stationsData:
        if float(sd['value']) >= global_treshold_level:
            IsOverTreshold = True

    if IsOverTreshold:
        return MessageFormatter.formatStationsMessage(stationsData)
    else:
        return MessageFormatter.formatStationsMessage(NoPrintCode)
    
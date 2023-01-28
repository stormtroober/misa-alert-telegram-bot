import Resources
from Resources import NoPrintCode
from Resources import getStationInfo

def formatStationsMessage(stationsData):
    if stationsData == NoPrintCode:
        return NoPrintCode
    else:
        stationDicts = []
        for stationData in stationsData:
            stationInfo = getStationInfo(stationData['code'])
            stationDicts.append({'visualOrder': stationInfo['visualOrder'],
                                 'msg': Resources.earth_emoji + ' ' + stationInfo['displayName'] + "\n" + stationData['trend'] + ' ' + stationData['value'] + ' metri' + "\n" + "Aggiornato al " + stationData['lastUpdateTime']})
    
        fullMsg = composeFullMessage(stationDicts)
        return fullMsg
    
def composeFullMessage(stationDicts):
    sortedStationDicts = sorted(stationDicts, key=lambda x: x["visualOrder"])
    fullMsg = ''
    for sd in sortedStationDicts:
        fullMsg += sd['msg'] + '\n\n'
    return fullMsg


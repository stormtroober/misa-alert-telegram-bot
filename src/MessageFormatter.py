import Resources
from Resources import NoPrintCode
from Resources import getStationInfo
from datetime import datetime, timedelta



def formatStationsMessage(stationsData):
    if stationsData == NoPrintCode:
        return NoPrintCode
    else:
        stationDicts = []
        for stationData in stationsData:
            stationData['lastUpdateTime'] = (datetime.strptime(stationData['lastUpdateTime'], "%d/%m/%Y %H:%M") + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
            stationInfo = getStationInfo(stationData['code'])
            stationDicts.append({'visualOrder': stationInfo['visualOrder'],
                                 'msg': Resources.earth_emoji + ' ' + stationInfo['displayName'] + "\n" + stationData['trend'] + ' ' + str(round(stationData['value'], 2)) + ' metri' + "\n" + "Aggiornato al " + stationData['lastUpdateTime']})
    
        fullMsg = composeFullMessage(stationDicts)
        print(fullMsg)
        return fullMsg
    
def composeFullMessage(stationDicts):
    sortedStationDicts = sorted(stationDicts, key=lambda x: x["visualOrder"])
    fullMsg = ''
    for sd in sortedStationDicts:
        fullMsg += sd['msg'] + '\n\n'
    return fullMsg


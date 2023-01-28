import Resources
from Resources import NoPrintCode
from Resources import bettolelle, pianello, serra, burello, senigallia

def formatStationsMessage(stationsData):
    if stationsData == NoPrintCode:
        return NoPrintCode
    else:
        stationDicts = []
        for stationData in stationsData:
            visualOrder = -1
            displayName = ''
            if stationData['code'] == serra['code']:
                visualOrder = 1
                displayName = serra['displayName']
                
            if stationData['code'] == pianello['code']:
                visualOrder = 2
                displayName = pianello['displayName']

            if stationData['code'] == burello['code']:
                visualOrder = 3
                displayName = burello['displayName']

            if stationData['code'] == bettolelle['code']:
                visualOrder = 4
                displayName = bettolelle['displayName']

            if stationData['code'] == senigallia['code']:
                visualOrder = 5
                displayName = senigallia['displayName']

            stationDicts.append({'visualOrder': visualOrder,
                                 'msg': Resources.earth_emoji + ' ' + displayName + "\n" + stationData['trend'] + ' ' + stationData['value'] + ' metri' + "\n" + "Aggiornato al " + stationData['lastUpdateTime']})

        fullMsg = composeFullMessage(stationDicts)
        return fullMsg
    
def composeFullMessage(stationDicts):
    sortedStationDicts = sorted(stationDicts, key=lambda x: x["visualOrder"])
    fullMsg = ''
    for sd in sortedStationDicts:
        fullMsg += sd['msg'] + '\n\n'
    return fullMsg


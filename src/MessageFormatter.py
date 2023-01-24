def formatStationsMessage(stationsData):
    stringDatas = []
    for stationData in stationsData:
        stringDatas.append('Localita: ' + stationData['stationPlace'].strip() + ' Valore: ' + stationData['value'] + " metri" + "\n" + "Trend: " + stationData['trend'] + " Aggiornato al " + stationData['lastUpdateTime'])
    return '\n\n'.join(stringDatas)
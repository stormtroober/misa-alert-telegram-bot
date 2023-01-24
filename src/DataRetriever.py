import requests
import json
import MessageFormatter
import ReservedSettings

def RetrieveStationData():
    IsDebugOn = False

    if(IsDebugOn):
        filtered_json = [{"codice":26,"nome":"Misa","localita":"Bettolelle ","comune":"Senigallia ","prov":"AN","latitudine":"43.66250","longitud":"13.16472","analog":[{"tipoSens":0,"descr":"Pioggia TOT Oggi ","valore":"28.6","trend":0,"unmis":"mm "},{"tipoSens":1,"descr":"Intensita di pioggia ","valore":"0.00","trend":0,"unmis":"mm/min "},{"tipoSens":5,"descr":"Temperatura aria ","valore":"6.7","trend":0,"unmis":"°C "},{"tipoSens":100,"descr":"Livello Misa ","valore":"3.68","trend":-0.02682800032198429,"unmis":"mt "},{"tipoSens":6,"descr":"Umidita relativa ","valore":"76","trend":0,"unmis":"% "}],"lastUpdateTime":"23/01/2023 12:45"}]
    else:
        path = ReservedSettings.api_endpoint
        x = requests.get(path)
        responseJson = json.loads(x.text)

        filtered_json = [
            dictionary for dictionary in responseJson
            if dictionary['codice'] == 26 or dictionary['codice'] == 183
        ]
    stationsData = []
    for station in filtered_json:
        lastUpdateTime = station['lastUpdateTime']
        stationPlace = station['localita']
        data = [
            dictionary for dictionary in station['analog']
            if dictionary['tipoSens'] == 100
        ]
        data = data[0]
        trend = "Crescita" if data['trend'] > 0 else "Decrescita"
        value = data['valore']
        stationsData.append({'stationPlace': stationPlace, 'value': value, 'trend': trend, 'lastUpdateTime': lastUpdateTime})
    return MessageFormatter.formatStationsMessage(stationsData)

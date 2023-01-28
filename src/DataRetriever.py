import requests
import json
import DataFilter
import ReservedSettings
import Resources
import time
from Resources import getStationCodes

def RetrieveStationData():
    IsDebugOn = False

    if(IsDebugOn):
        filtered_json = [{"codice":26,"nome":"Misa","localita":"Bettolelle ","comune":"Senigallia ","prov":"AN","latitudine":"43.66250","longitud":"13.16472","analog":[{"tipoSens":0,"descr":"Pioggia TOT Oggi ","valore":"28.6","trend":0,"unmis":"mm "},{"tipoSens":1,"descr":"Intensita di pioggia ","valore":"0.00","trend":0,"unmis":"mm/min "},{"tipoSens":5,"descr":"Temperatura aria ","valore":"6.7","trend":0,"unmis":"°C "},{"tipoSens":100,"descr":"Livello Misa ","valore":"3.68","trend":-0.02682800032198429,"unmis":"mt "},{"tipoSens":6,"descr":"Umidita relativa ","valore":"76","trend":0,"unmis":"% "}],"lastUpdateTime":"23/01/2023 12:45"}]
    else:
        status_code = 0
        tries = 0
        while status_code != 200:
            path = ReservedSettings.api_endpoint
            x = requests.get(path)
            status_code = x.status_code
            if(status_code != 200):
                time.sleep(5)
                print('Trying again...')
            if(tries > 3):
                print('Giving up after 3 tries')
                break
            tries += 1
        responseJson = json.loads(x.text)

        filtered_json = [
            dictionary for dictionary in responseJson
            if FilterAllStations(dictionary)
        ]
    stationsData = []
    for station in filtered_json:
        lastUpdateTime = station['lastUpdateTime']
        codice = station['codice']
        stationPlace = station['localita'].strip()
        data = [
            dictionary for dictionary in station['analog']
            if dictionary['tipoSens'] == 100
        ]
        data = data[0]
        trend = Resources.increasing_chart_emoji if data['trend'] > 0 else Resources.decreasing_chart_emoji
        value = data['valore']
        stationsData.append({'code': codice, 'stationPlace': stationPlace, 'value': value, 'trend': trend, 'lastUpdateTime': lastUpdateTime})
    return DataFilter.filter(stationsData)


def FilterAllStations(dict):
    codes = getStationCodes()
    return pred(dict, codes[0]) or pred(dict, codes[1]) or pred(dict, codes[2]) or pred(dict, codes[3]) or pred(dict, codes[4])

def pred(dict, code):
    return dict['codice'] == code


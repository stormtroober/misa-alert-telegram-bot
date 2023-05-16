import requests
import json
from DataFilter import DataFilter
import ReservedSettings
import Resources
import time
from Resources import getStationCodes, ErrorCode

dataFilter = DataFilter()

def getDataFilter():
    return dataFilter

def RetrieveStationData():
    stationsData = []
    for station in Resources.stations:
        path = ReservedSettings.baseUrlForStations + str(station['code'])
        try:
            response = requests.get(path, timeout=10)
        except ConnectionResetError as exc:
            print('Oh no, connection error', str(exc))
            # raise
        else:
            print(station['code'], response.status_code)
            if response.status_code == 200:
                data = json.loads(response.text)
                lastUpdateTime = data['lastUpdateTime']
                codice = data['codice']
                stationPlace = data['localita'].strip()
                sensorFiltered = []
                for sensor in data['analog']:
                    if(sensor['TIPOSENS'] == 100 or sensor['TIPOSENS'] == 101):
                        sensorFiltered.append(sensor)
                if station['code'] == 185:
                    #stazione ponte garibaldi ha il nuovo sensore radar
                    sensor = sensorFiltered[1]
                else:
                    sensor = sensorFiltered[0]
                trend = Resources.increasing_chart_emoji if sensor['TREND'] > 0 else Resources.decreasing_chart_emoji
                value = sensor['VALORE']
                stationsData.append({'code': codice, 'stationPlace': stationPlace, 'value': value, 'trend': trend, 'lastUpdateTime': lastUpdateTime})
    if(len(stationsData) > 0):
        return dataFilter.filter(stationsData)
    else:
        return ErrorCode
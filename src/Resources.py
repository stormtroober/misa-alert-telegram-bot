NoPrintCode = -47
ErrorCode = -48
increasing_chart_emoji = "\U0001F4C8"
decreasing_chart_emoji = "\U0001F4C9"
earth_emoji = "\U0001F30D"
stations = [
    {'code': 3, 'displayName': 'Serra de Conti', 'visualOrder': 1},
    {'code': 183, 'displayName': 'Pianello', 'visualOrder': 2},
    {'code': 120, 'displayName': 'Burello (Nevola)', 'visualOrder': 3},
    {'code': 26, 'displayName': 'Bettolelle', 'visualOrder': 4}
    # {'code': 185, 'displayName': 'Senigallia Ponte Garibaldi', 'visualOrder': 5}
]

def getStationInfo(code):
    for s in stations:
        if(s['code'] == code):
            return s

def getStationCodes():
    listCodes = []
    for s in stations:
        listCodes.append(s['code'])
    return listCodes
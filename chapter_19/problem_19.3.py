class weather:
    def __init__(self):
        self.__params=['temp','rel hum','cloud cover','wind vel']

    def __contains__(self,p):
        return True if p in self.__params else False

w=weather()
if 'rel hum' in w:
    print('Valid weather parameters')
else:
    print("Invalid weather parameters")
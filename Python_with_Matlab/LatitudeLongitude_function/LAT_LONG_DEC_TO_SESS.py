from typing import KeysView
import sys


def fromDegToLat(value):
    K = ''
    XX = int(abs(float(value)))
    YY = ''
    ZZ = ''
    value = float(value)

    if (value < -90.0) | (value > 90.0):
        print("LAT is out of range. Displaying AMBER_DASHES")
    else:
        # Compute K
        K = 'N' if (value >= 0.0) else 'S'

        # Compute YY and XX
        value = abs(value)
        Decimals = (value - float(XX))*60
        YY = int(Decimals+0.5)
        ZZ = int((Decimals - float(YY))*100)

        print(K +' '+ str(XX) + '°' + str(YY) + '.' + str(ZZ) + "'")

def fromDegToLong(value):
    K = ''
    XX = int(abs(float(value)))
    YY = ''
    ZZ = ''
    value = float(value)

    if (value < -180.0) | (value > 180.0):
        print("LONG is out of range. Displaying AMBER_DASHES")
    else:
        # Compute K
        K = 'E' if (value >= 0.0) else 'W'

        # Compute YY and XX
        value = abs(value)
        Decimals = (value - float(XX))*60
        YY = int(Decimals)
        ZZ = int((Decimals - float(YY))*100)

        print(K +' '+ str(XX) + '°' + str(YY) + '.' + str(ZZ) + "'")



if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Missing parameters! Pass the value to convert')
    else:
        if sys.argv[2] == 'lat':
            fromDegToLat(sys.argv[1])
        elif sys.argv[2] == 'long':
            fromDegToLong(sys.argv[1])
        else:
            print("No lat or long string were passed")

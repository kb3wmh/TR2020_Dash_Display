
import struct

# Telemetry format is [uint8_t APID, int32_t VALUE]
formatString = "!Bf"

# Telemetry APIDs
engineRpm = 1
engineTemp = 2
wheelSpeed = 3
battVoltage = 4
lambdaSensor = 5
mapSensor = 6
tpsSensor = 7
tireTemp = 8
gear = 9

def buildTlmPkt(apid, value):
    return struct.pack(formatString, 1, value)

def decodeTlmPkt(pkt):
    return struct.unpack(formatString, pkt)
    

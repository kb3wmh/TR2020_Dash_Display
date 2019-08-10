import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from diagwindow import Ui_MainWindow
import time
import random
import _thread as thread

# PE3 CAN Arbitration IDs
pe1 = 0x0CFFF048
pe2 = 0x0CFFF148
pe3 = 0x0CFFF248
pe4 = 0x0CFFF348
pe5 = 0x0CFFF448
pe6 = 0x0CFFF548
pe7 = 0x0CFFF648
pe8 = 0x0CFFF748
pe9 = 0x0CFFF848
pe10 = 0x0CFFF948
pe11 = 0x0CFFFA48
pe12 = 0x0CFFFB48
pe13 = 0x0CFFFC48
pe14 = 0x0CFFFD48
pe15 = 0x0CFFFE48
pe16 = 0x0CFFD048


# Flags allowing modules to be turned on and off
engineRpmEnabled = True
engineTempEnabled = True
wheelSpeedEnabled = True
voltageEnabled = True
lambdaEnabled = True
mapEnabled = True
tpsEnabled = True
tireTempEnabled = True
gearEnabled = False

def convertUnsignedToSigned(num):
    result = num

    if (num > 32767):
        result = result - 65536

    return result

def dispRpm(data, ui):
    rpmLowByte = data[0]
    rpmHighByte = data[1]

    rpm = 256 * rpmHighByte + rpmLowByte

    ui.rpm_lcdnumber.display(rpm)

def dispVoltage(data, ui):
    voltScaleFactor = 0.01

    voltLowByte = data[0]
    voltHighByte = data[1]
    
    voltage = (256 * voltLowByte + voltHighByte) * voltScaleFactor

def dispLambda(data, ui):
    lambdaScaleFactor = 0.01

    lambdaLowByte = data[4]
    lambdaHighByte = data[5]

    lambdaVal = (256 * lambdaLowByte + lambdaHighByte) * lambdaScaleFactor

def dispMap(data, ui):
    mapScaleFactor = 0.01

    mapLowByte = data[2]
    mapHighByte = data[3]

    mapVal = (256 * mapLowByte + mapHighByte) * mapScaleFactor

def dispTps(data, ui):
    tpsScaleFactor = 0.1

    tpsLowByte = data[2]
    tpsHighByte = data[3]

    tps = (256 * tpsLowByte + tpsHighByte) * tpsScaleFactor

    tps = round(tps)

def dispEngineTemp(data, ui):
    tempScaleFactor = 0.1

    tempLowByte = data[4]
    tempHighByte = data[5]

    temp = (256 * tempLowByte + tempHighByte) * tempScaleFactor

    temp = convertUnsignedToSigned(temp)

    temp = round(temp)

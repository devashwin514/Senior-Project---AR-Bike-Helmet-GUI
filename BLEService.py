from pybleno import *
#from BatteryLevelCharacteristic import *
from BLECharacteristic import *

class BLEService(BlenoPrimaryService):
    def __init__(self, direction, speed):
        BlenoPrimaryService.__init__(self, {
          'uuid': '6109',
          'characteristics': [
              #ReadDirCharacteristic(direction),
              WriteDirCharacteristic(direction),
              WriteSpeedCharacteristic(speed)
          ]})

from pybleno import *
#from BatteryLevelCharacteristic import *
from BLECharacteristic import *

class BLEService(BlenoPrimaryService):
    def __init__(self):
        BlenoPrimaryService.__init__(self, {
          'uuid': '180F',
          'characteristics': [
              ReadDirCharacteristic(),
              WriteDirCharacteristic(),
              WriteSpeedCharacteristic()
          ]})

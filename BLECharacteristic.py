from pybleno import *
import array
import sys
import subprocess
import re
        
class WriteDirCharacteristic(Characteristic):
    def __init__(self, direction):
        Characteristic.__init__(self, {
            'uuid': '2A20',
            'properties': ['write'],
            'value': None
          })
          
        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = None
        self.direction = direction
        
    def onWriteRequest(self, data, offset, withoutResponse, callback):
        self._value = data

        print('Write Direction - %s - onWriteRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))

        if self._updateValueCallback:
            print('Write Direction - onWriteRequest: notifying');
            
            self._updateValueCallback(self._value)
        
        callback(Characteristic.RESULT_SUCCESS)
        
        
class WriteSpeedCharacteristic(Characteristic):
    def __init__(self, speed):
        Characteristic.__init__(self, {
            'uuid': '2A21',
            'properties': ['write'],
            'value': None
          })
          
        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = None
        self.speed = speed
        
    def onWriteRequest(self, data, offset, withoutResponse, callback):
        self._value = data
        
        self.speed = data
        
        print('selfValue = ', self._value)

        print('Write Speed - %s - onWriteRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))

        if self._updateValueCallback:
            print('Write Speed - onWriteRequest: notifying');
            
            self._updateValueCallback(self._value)
        
        callback(Characteristic.RESULT_SUCCESS)
        
        f = '/home/pi/Desktop/spd.txt'
        
        
        with open(f, 'w') as spd:
            for c in self._value:
                res = str(hex(c))
                spd.write(res)
            spd.close()
        

'''
class NotifyDirCharacteristic(Characteristic):
    def __init__(self, direction):
        Characteristic.__init__(self, {
            'uuid': '2A18',
            'properties': ['notify'],
            'onSubscribe': None
          })
          
        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = None
        self.direction = direction
        
    def onReadRequest(self, offset, callback):
        if (offset):
            callback(Characteristic.RESULT_ATTR_NOT_LONG, None)
        else:
            self._value = self.direction
            print('Read Direction - %s - onReadRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))
            callback(Characteristic.RESULT_SUCCESS, self._value) 
'''
'''
class ReadDirCharacteristic(Characteristic):
    def __init__(self, direction):
        Characteristic.__init__(self, {
            'uuid': '2A19',
            'properties': ['read'],
            'value': None
          })
          
        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = None
        self.direction = direction
        
    def onReadRequest(self, offset, callback):
        if (offset):
            callback(Characteristic.RESULT_ATTR_NOT_LONG, None)
        else:
            self._value = self.direction
            print('Read Direction - %s - onReadRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))
            callback(Characteristic.RESULT_SUCCESS, self._value)
'''

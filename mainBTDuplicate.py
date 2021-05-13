from Tkinter import *
import Tkinter as tk
from pybleno import *
import sys
import signal
import ultrasonic
import ultrasonic2
import time
import RPi.GPIO as GPIO
from threading import *
from multiprocessing import *
from BLEService import *
import os



def main(writeDirection, writeSpeed):
    bleno = Bleno()
    primaryService = BLEService(writeDirection, writeSpeed)

    def onStateChange(state):
       print('on -> stateChange: ' + state);

       if (state == 'poweredOn'):
           bleno.startAdvertising('BLE', [primaryService.uuid]);
       else:
         bleno.stopAdvertising();
    bleno.on('stateChange', onStateChange)

    def onAdvertisingStart(error):
        print('on -> advertisingStart: ' + ('error ' + error if error else 'success'));

        if not error:
            def on_setServiceError(error):
                print('setServices: %s'  % ('error ' + error if error else 'success'))
                
            bleno.setServices([
                primaryService
            ], on_setServiceError)
    bleno.on('advertisingStart', onAdvertisingStart)

    bleno.start()

    print ('Hit <ENTER> to disconnect')

    if (sys.version_info > (3, 0)):
        input()
    else:
        raw_input()

    bleno.stopAdvertising()
    bleno.disconnect()

    print ('terminated.')
    sys.exit(1)
    
#def vceCmd():
#    while True:
#        input_state = GPIO.input(32)
#        if input_state == False:
#            print('Button is Pressed')
#            os.system('arecord -D plughw:CARD=Device,DEV=0 -f S16_LE -c1 -r16000 -d 7 test.wav')
#            break
#        time.sleep(0.2)
#        #os.system('aplay test.wav')
#    os.system('pocketsphinx_continuous -lm 0351.lm -dict 0351.dic -infile test.wav 2>./log.txt | tee ./words.txt')
#        
#        
#    path = '/home/pi/Desktop/words.txt'
#    res = open(path, 'r')
#    lines = res.readlines()
#    result = lines[1]
#    
#    #print(result)
#        
#    return result
#
#mt1 = Thread(target=vceCmd)
#mt1.start()
#

fullscreen = False
def makeFullscreen(root):
    #global root
    global fullscreen
    
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.IN,pull_up_down=GPIO.PUD_UP)


def vceCmd():
    while True:
        input_state = GPIO.input(32)
        while input_state == False:
            print('Button is Pressed')
            os.system('arecord -D plughw:CARD=Device,DEV=0 -f S16_LE -c1 -r16000 -d 7 test.wav')
    #           break
            time.sleep(0.2)
            #os.system('aplay test.wav')
            os.system('pocketsphinx_continuous -lm 0351.lm -dict 0351.dic -infile test.wav 2>./log.txt | tee ./words.txt')
            break
            
        


def myWind():
    root = tk.Toplevel()
    root.configure(background = 'black')
    #tkt = TkThread(root)

    topFrame = tk.Frame(root)
    topFrame.pack()

    bottomFrame = tk.Frame(root)
    bottomFrame.pack(side=tk.BOTTOM)

    leftFrame = tk.Frame(root)
    leftFrame.pack(side=tk.LEFT)

    rightFrame = tk.Frame(root)
    rightFrame.pack(side=tk.RIGHT)

    img3 = tk.PhotoImage(file='/home/pi/Downloads/haz1.png')
    bSIcon = img3.subsample(3, 3)
    bSIconLabel = tk.Label(leftFrame, image=bSIcon)
    #bSIconLabel.pack()
    
    #dist = ultrasonic.distance1()
    
    def readFile():
        while True:
            path = '/home/pi/Desktop/words.txt'
            res = open(path, 'r')
            lines = res.readlines()
            result = lines[1]   
            return result
    
    t2 = Thread(target=readFile)
    t2.start()
    
    result = t2
    
    def obstDet():
        while True:
            ultrasonic.distance1()
            ultrasonic2.distance1()
            print("dist1 = ", ultrasonic.distance1())
            print("dist2 = ", ultrasonic2.distance1())
            if (ultrasonic.distance1() == 1 or ultrasonic2.distance1() == 1):
                if(result != ('TOGGLE OBSTACLE' or 'TURN OFF THE SENSOR')):
                    bSIconLabel.pack()
            else:
                bSIconLabel.pack_forget()
            #print(dist)
            time.sleep(1)

    t1 = Thread(target=obstDet)
    t1.start()
    


    navMessage = tk.Message(rightFrame, text="Turn Left On Meredith Way")
    navMessage.config(font=('times', 20))
    navMessage.pack(side=tk.RIGHT)

#    timeMessage = tk.Message(topFrame, text=time_string)
#    timeMessage.config(font=('times', 20))
#    timeMessage.pack(side=tk.LEFT)
    
    
    timeLabel = tk.Label(topFrame, font=('times', 20))
    timeLabel.pack(side=tk.LEFT)
    
    
    def tick():
        time2 = time.strftime('%I:%M')
        
        timeLabel.config(text=time2)
        
        timeLabel.after(200, tick)
            
            #time.sleep(1)
        
    t4 = Thread(target=tick)
    t4.start()
    
#    GPIO.setmode(GPIO.BOARD)
#    GPIO.setup(32,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    
    
#    def vceCmd():
#        while True:
#            input_state = GPIO.input(32)
#            if input_state == False:
#                print('Button is Pressed')
#                os.system('arecord -D plughw:CARD=Device,DEV=0 -f S16_LE -c1 -r16000 -d 7 test.wav')
#                break
#                time.sleep(0.2)
#        #os.system('aplay test.wav')
#        os.system('pocketsphinx_continuous -lm 0351.lm -dict 0351.dic -infile test.wav 2>./log.txt | tee ./words.txt')
#        
#        
#        path = '/home/pi/Desktop/words.txt'
#        res = open(path, 'r')
#        result = res.readLine()
#        
#        return result

#    result = switch.vceCmd()
##        
##        
###    t5 = Thread(target=vceCmd)
###    t5.start()
##    
#    testVCMessage = tk.Message(rightFrame, text=result)
#    testVCMessage.config(font=('times', 20))
#    testVCMessage.pack(side=tk.BOTTOM)
    
    speedMessage = tk.Message(bottomFrame, text="0 mph")
    #speedMessage = tk.Message(bottomFrame, text=str(xSpeed))
    speedMessage.config(font=('times', 20))
    speedMessage.pack(side=tk.BOTTOM)
    
    
    


    makeFullscreen(root)
    
    
#    root.update()
#    time.sleep(2)
    
    
    
    writeDirection = []
    writeSpeed = []
    mt4 = Thread(target=main, args=(writeDirection, writeSpeed,))
    mt4.start()
    
#    while True:
#        path = '/home/pi/Desktop/spd.txt'
#        res = open(path, 'r')
#        lines = res.readlines()
#        result = lines[1]
#        
#    print(result)
    
    
    #time.sleep(5)

#    def bTGetDir():
#        while True:
#            keyword = vceCmd()
#            if (keyword == "GIVE ME DIRECTIONS"):
#                A = primaryService['characteristic'][1]['_value']
#                print(A)
#                
#            return A
#    
#    
#    
#    def bTGetSpd():
#        while True:
#            A = primaryService['characteristic'][2]['_value']
#            print(A)
#            return A
#    
    
    
    
    
#    mt3 = Thread(target=bTGetSpd)
#    mt3.start()
#    
#    mt2 = Thread(target=bTGetDir)
#    mt2.start()
    
    
    
    root.mainloop()
    
    
    
if __name__ == '__main__':
    
    
    
    mp1 = Process(target=myWind)
    mp1.start()
    
    mp2 = Process(target=vceCmd)
    mp2.start()
    
    


    
#    mt2 = Thread(target=main)
#    mt2.start()

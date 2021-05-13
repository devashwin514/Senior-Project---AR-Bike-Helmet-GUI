#!/usr/bin/python3 


import tkinter as tk
#from pylab import *
#import tkFont
from PIL import Image, ImageTk
#from tkinter_accelerometer import ADXL345
#from tkinter_bluetooth import bluetoothConnect
import ultrasonic
import ultrasonic2
import time
import RPi.GPIO as GPIO
from threading import *
from datetime import datetime
#from multiprocessing import *
import signal

root = None
dispFont = None
frame = tk.Frame(root)
fullscreen = False
now = datetime.now()
time_string = now.strftime('%I:%M')


## Ultrasonic Code

##set GPIO Warnings to false
#GPIO.setwarnings(False)
#
##GPIO Mode (BOARD / BCM)
#GPIO.setmode(GPIO.BOARD)
# 
##set GPIO Pins
###trigger originally 18
###echo originally 24
#GPIO_TRIGGER = 38
#GPIO_ECHO = 40
 
#set GPIO direction (IN / OUT)
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)

##def distance():
##    return 1
 
##def distance1():
##    # set Trigger to HIGH
##    GPIO.output(GPIO_TRIGGER, True)
## 
##    # set Trigger after 0.01ms to LOW
##    time.sleep(0.00001)
##    GPIO.output(GPIO_TRIGGER, False)
## 
##    StartTime = time.time()
##   # StopTime
## 
##    # save StartTime
##    while GPIO.input(GPIO_ECHO) == 0:
##        StartTime = time.time()
## 
##    # save time of arrival
##    while GPIO.input(GPIO_ECHO) == 1:
##        StopTime = time.time()
## 
##    # time difference between start and arrival
##    TimeElapsed = StopTime - StartTime
##    # multiply with the sonic speed (34300 cm/s)
##    # and divide by 2, because there and back
##    distance = (TimeElapsed * (34300/2.54)) / 2
## 
##    return distance



def makeFullscreen(root):
    #global root
    global fullscreen
    
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    #resize()

##GPIO.setmode(GPIO.BOARD) #Use RPi board pin numbers
##GPIO.setup(40, GPIO.OUT) #Set pin 40 as output pin
##GPIO.setup(38, GPIO.IN) #Set pin 38 as input pin
##
##def inputChg(channel):
##    print("Input pin status changed to ", GPIO.input(38))
##    
##GPIO.add_event_detect(38, GPIO.RISING, bouncetime=3)
##
##GPIO.output(40, True)
##time.sleep(1)

##def obstDet():
##    while True:
##        distance = ultrasonic.distance()
##        
##        #distArr = [dist]
##        print(distance)
##        #return distance  
##        time.sleep(1)
##        root.mainloop()
##    return distance
##    
##def dispBSIcon():
##    dist = obstDet()
##    if (dist <= 5):
##        postImg()
##        time.sleep(1)

##def resize(event = None):
##    global dispFont
##    global frame
##    
##    newSize = -max(12, int((frame.winfo_height() / 10)))
##    dispFont.configure(font=newSize)

def myWind():
    root = tk.Toplevel()
    root.configure(background = 'black')

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
    
    
    def obstDet():
        while True:
            ultrasonic.distance1()
            ultrasonic2.distance1()
            print("dist1 = ", ultrasonic.distance1())
            print("dist2 = ", ultrasonic2.distance1())
            if (ultrasonic.distance1() == 1 or ultrasonic2.distance1() == 1):
                bSIconLabel.pack()
            else:
                bSIconLabel.pack_forget()
            #print(dist)
            time.sleep(1)

    t1 = Thread(target=obstDet)
    t1.start()
    
    def bTGetDir():
        while True:
            # if (*keyword detected*):
            A = main.primaryService['characteristic'][1]['_value']
            print(A)
            
            # if (*return direction value != current dir value*):
            # then dont update value to GUI
            
            return A
    
    t2 = Thread(target=bTGetDir)
    t2.start()
    
    def bTGetSpd():
        while True:
            A = main.primaryService['characteristic'][2]['_value']
            print(A)
            return A
    
    t3 = Thread(target=bTGetSpd)
    t3.start()

    navMessage = tk.Message(rightFrame, text="Turn Left On Meredith Way")
    navMessage.config(font=('times', 20))
    navMessage.pack(side=tk.RIGHT)

    timeMessage = tk.Message(topFrame, text=time_string)
    timeMessage.config(font=('times', 20))
    timeMessage.pack(side=tk.LEFT)
    
    
#    time1 = ''
#    
#    def tick(time1):
#        while True:
#            time2 = time.strftime('%I:%M')
#        
#            if (time1 != time2):
#                print("time2 = ", time2)
#                time1 = time2
#                timeLabel.config(text=time2)
#            
#            timeLabel.pack(side=tk.LEFT)
#            
#            time.sleep(1)
#        
#    t2 = Thread(target=tick, args=(time1))
#    t2.start()
    

    speedMessage = tk.Message(bottomFrame, text="0 mph")
    #speedMessage = tk.Message(bottomFrame, text=str(xSpeed))
    speedMessage.config(font=('times', 20))
    speedMessage.pack(side=tk.BOTTOM)

    makeFullscreen(root)

    root.mainloop()



#accel = tkinter_accelerometer.ADXL345()

#axes = tkinter_accelerometer.getAxes()

#xAccel = axes['x']

#xSpeed = xAccel/time

#data = tkinter_bluetooth.bluetoothConnect()
    
##Obstacle Detection
#distArr = []


##Rendering Frame
if __name__ == '__main__':
    myWind()



# root = tk.Toplevel()
# root.configure(background = 'black')
#root.FLIP_LEFT_RIGHT
    
#root = tk.Tk()

#top = tk.Toplevel(root, bg='black')


# Allocating each section of the frame in the GUI
# topFrame = tk.Frame(root)
# topFrame.pack()

# bottomFrame = tk.Frame(root)
# bottomFrame.pack(side=tk.BOTTOM)

# leftFrame = tk.Frame(root)
# leftFrame.pack(side=tk.LEFT)

# rightFrame = tk.Frame(root)
# rightFrame.pack(side=tk.RIGHT)

#var = tk.DoubleVar()
#img = tk.PhotoImage(file='C:/Users/ashwi/Downloads/bluetooth-512.png')
#img = Image.open('/home/pi/Downloads/bluetooth-512.png')
#img = img.resize((250, 250), Image.ANTIALIAS)
#img.save("btIcon.png")
#btIcon = tk.PhotoImage(file="btIcon.png")
#btIcon_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
#btIcon = tk.PhotoImage(btIcon_flip)
#btIconLabel = tk.Label(topFrame, image=btIcon)
#btIconLabel.pack()
#btMessage = tk.Message(topFrame, text="Bluetooth Icon")
#btMessage.config(font=('times', 20))
#btMessage.pack(side=tk.LEFT)


#if an obstacle is detected, then show an icon that there is an obstruction
#for i in distArr:

##img3 = tk.PhotoImage(file='/home/pi/Downloads/blind_spot_icon.png.png')
##bSIcon = img3.subsample(3, 3)
##bSIconLabel = tk.Label(leftFrame, image=bSIcon)
##bSIconLabel.pack()

#Posting blind spot image
# def postImg():
#     img3 = tk.PhotoImage(file='/home/pi/Downloads/blind_spot_icon.png.png')
#     bSIcon = img3.subsample(3, 3)
#     bSIconLabel = tk.Label(leftFrame, image=bSIcon)
#     bSIconLabel.pack()

# #postImg()


# # Trying to update the GUI with distance to post the Blind Spot icon onto GUI
# while (True):
#     dist = ultrasonic.distance1() #Getting distance measurement from Ultrasonic reading
#     print (dist)
#     if (dist <= 5): #Units: inches
#         postImg()
#     time.sleep(0.5)
####    
##GPIO.output(38, False)
##GPIO.remove_event_detect(38)
##GPIO.cleanup()
##print("Done")

    
#t = time.time()

##t1 = Thread(target=obstDet)
##t2 = Thread(target=dispBSIcon)
##
##t1.lock()
##t2.lock()
##
##t1.start()
##t2.start()
##
##t1.join()
##t2.join()
    
##signal.signal(signal.SIGCLD, signal.SIG_DFL)
##        
##p1 = Process(target=obstDet)
##p2 = Process(target=dispBSIcon)
##
##p1.start()
##p2.start()
##
##p1.join()
##p2.join()

##while True:
##       dist = ultrasonic.distance()
##dist = obstDet()
##if (dist <= 5):
##       bSIconLabel.pack()
##       #time.sleep(1)


    

 



##img2 = tk.PhotoImage(file='/home/pi/Downloads/turn_left_522008.png')
##turnLeftIcon = img2.subsample(7, 7)
##turnLeftIconLabel = tk.Label(rightFrame, image=turnLeftIcon)
##turnLeftIconLabel.pack()

# navMessage = tk.Message(rightFrame, text="Turn Left On Meredith Way")
# navMessage.config(font=('times', 20))
# navMessage.pack(side=tk.RIGHT)

# timeMessage = tk.Message(topFrame, text=time_string)
# timeMessage.config(font=('times', 20))
# timeMessage.pack(side=tk.LEFT)

# speedMessage = tk.Message(bottomFrame, text="15 mph")
# #speedMessage = tk.Message(bottomFrame, text=str(xSpeed))
# speedMessage.config(font=('times', 20))
# speedMessage.pack(side=tk.BOTTOM)

# ##img3 = tk.PhotoImage(file='/home/pi/Downloads/blind_spot_icon.png.png')
# ##bSIcon = img3.subsample(3, 3)
# ##bSIconLabel = tk.Label(leftFrame, image=bSIcon)
# ##bSIconLabel.pack()

# makeFullscreen()

# root.mainloop()

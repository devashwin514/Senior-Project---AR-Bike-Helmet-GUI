#!/usr/bin/python3

#Libraries
import RPi.GPIO as GPIO
import time


#set GPIO Warnings to false
GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
##trigger originally 18
##echo originally 24
GPIO_TRIGGER = 38
GPIO_ECHO = 40
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

 
def distance1():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
   # StopTime
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * (34300/2.54)) / 2
    
    #return distance


    if (distance <= 5):
        return 1
    else:
        return 0
        
#dist = distance()

##for x in range (0, 5):
##    dist = distance()
##    print (dist)
#print (dist)
 
#if __name__ == '__main__':
#    try:
#        while True:
#            dist = distance1()
#            print ("Measured Distance = %.1f in" % dist)
##            if (dist <= 5):
##                return 1
#            time.sleep(1)
#            
# 
#        # Reset by pressing CTRL + C
#    except KeyboardInterrupt:
#        print("Measurement stopped by User")
#        GPIO.cleanup()

#if __name__ == '__main__':
#try:
#    while True:
#        dist = distance()
#        print ("Measured Distance = %.1f in" % dist)
#        time.sleep(1)
#     
#            # Reset by pressing CTRL + C
#except KeyboardInterrupt:
#    print("Measurement stopped by User")
#    GPIO.cleanup()

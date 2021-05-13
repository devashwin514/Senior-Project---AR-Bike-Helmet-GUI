import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(32)
    if input_state == False:
        print('Button is Pressed')
        os.system('arecord -D plughw:CARD=Device,DEV=0 -f S16_LE -c1 -r16000 -d 5 test.wav')
        break
        time.sleep(0.2)

os.system('aplay test.wav')
os.system('pocketsphinx_continuous -infile test.wav')
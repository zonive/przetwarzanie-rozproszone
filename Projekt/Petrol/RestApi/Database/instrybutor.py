#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522


GPIO.setmode(GPIO.BCM)
reader = SimpleMFRC522()

########### LED config #############################
# segments =  (11,4,23,8,7,10,18,25)
segments =  (6,4,23,12,7,5,18,16)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = (22,27,17,24)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
 
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}
hey = {'0':(0,0,0,0,0,0,0),     #puste
    '1':(0,1,1,0,0,0,0),        #I
    '2':(0,1,1,0,1,1,1),        #H
    '3':(1,0,0,1,1,1,1)}        #E
    
########### BUTTON config###########################
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
####################################################

remainLitres = 1000
cardId = "868581146633"
cardKey = "brelok                                          "

def inf(mess):
    s = str(mess).ljust(4)
    for digit in range(4):
        for loop in range (0,7):
            GPIO.output(segments[loop], hey[s[digit]][loop])
        GPIO.output(digits[digit], 0)
        time.sleep(0.005)
        GPIO.output(digits[digit], 1)

def lcd(remainLitres):
    if remainLitres == 0:
        z = "0000"
    elif remainLitres < 10:
        z = "000" 
    elif remainLitres < 100:
        z = "00" 
    elif remainLitres < 1000:
        z = "0"
    else:
        z = ""
    x = str(remainLitres).ljust(4)
    s = ''.join([z, x])
    for digit in range(4):
        for loop in range (0,7):
            if (digit == 1):
                GPIO.output(16, 1)              #decimal point
            else:
                GPIO.output(16, 0)   
            GPIO.output(segments[loop], num[s[digit]][loop])
        GPIO.output(digits[digit], 0)
        time.sleep(0.005)
        GPIO.output(digits[digit], 1)
    # print(s)

def auth():
    # inf("2100")       #HI
    id, key = reader.read()
    id = str(id)
    key = str(key)
    print(key + ",")
    if id == cardId and key == cardKey:
        print("Auth OK")
        return True
    else:
        
        print("Auth Failed")
        return False

try:
    while True:
        print("Waiting for auth")
        if auth() == True:
            logout = 300
            while True:
                inf("2100")       #HI
                lcd(remainLitres)
                if GPIO.input(26) == GPIO.HIGH and remainLitres >= 1:
                    logout = 300
                    remainLitres -= 1
                    # print(remainLitres)
                    # lcd(remainLitres)
                else:
                    logout -= 1
                print(logout)
                if logout <= 1:
                    break
                
        # inf("3333")       #EEEE

finally:
    GPIO.cleanup()
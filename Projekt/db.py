#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import requests

GPIO.setmode(GPIO.BCM)
reader = SimpleMFRC522()

db = "https://petroljp.azurewebsites.net/"

def all():
    response = requests.get(f"{db}/Petrol")
    print(response.text)

def addPetrol():
    id = int(input("Type id:"))
    litres = str(input("Type new liters state:"))
    # print (litres + ",")
    response = requests.put(f"{db}/Petrol/{id}", json = str(litres))
    # print(response.status_code)

def new():
    # {"firstName":"Test","lastName":"Testowy","cardId":"868581146633","cardKey":"test","litres":2137}
    firstName = str(input("Type First Name:"))
    lastName = str(input("Type Last Name:"))
    print("Please read the card")
    card, key = reader.read()
    cardId = str(card)
    cardKey = str(key)
    litres = str(input("Type new liters state:"))
    
    # cardId = "868581146633"
    # cardKey = "tes1t"

    # data1 = '{"firstName":"' +firstName+ '" ,"lastName":"' +lastName+ '","cardId":"' +cardId+'","cardKey":"' +cardKey+ '","litres":' + litres+ '}'
    # data1 = {"firstName\":" +firstName+ ",\"lastName\":" +lastName+ ",\"cardId\":" +cardId+ ",\"cardKey\":" +cardKey+  ",\"litres\":" + litres}
    data1 = {'"firstName":"' +firstName+ '" ,"lastName":"' +lastName+ '","cardId":"' +cardId+ '","cardKey":"' +cardKey+ '","litres":' + litres}

    data1 = {"firstName":"Test" ,"lastName":"TestHard","cardId":"868581146633","cardKey":"test","litres":2222}
    print(data1)
    headers = {"Content-Type": "application/json"}
    response = requests.put("https://petroljp.azurewebsites.net/new",headers=headers, json = data1)
    # print(str(response.content()))
    print(response.text)
    print(response.json)
    print(response.status_code)



try:
    while input !=4:
        print("\nWhat you want?:\n1)Show all data\n2)Update petrol by id\n3)Add new user\n4)End")
        try:
            mode = int(input('Input:'))
            if mode == 1:
                all()
            elif mode == 2:
                addPetrol()
            elif mode == 3:
                new()
            else:
                print("Wrong number")

        except ValueError:
            print("Not a number")
finally:
    GPIO.cleanup()
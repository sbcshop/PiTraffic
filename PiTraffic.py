#!/usr/bin/python

# Library for PiTraffic
# Developed by: SB Components
# Author: Ankur
# Project: PiTraffic
# Python: 3.4.2

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def closeGPIO():
    GPIO.cleanup()

class Buzzer:
    def __init__(self):
        self.pin = 12
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        print("Buzzer - ON")
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        print("Buzzer - OFF")
        GPIO.output(self.pin,GPIO.LOW)       
    

class Traffic:
    ''' Class to handle LED's

    Arguments:
    direction =  (i.e. "EAST","WEST","NORTH","SOUTH")
    color = Color of LED
    '''
    traffic_pins = {"SOUTH":{'RED':11,'YELLOW':13, "GREEN":15},
                    "WEST" :{'RED':16,'YELLOW':18, "GREEN":22},
                    "NORTH":{'RED':29,'YELLOW':31, "GREEN":33},
                    "EAST" :{'RED':36,'YELLOW':38, "GREEN":40}}


    def __init__(self, direction, color):
        self.pin = self.traffic_pins[direction][color]
        self.direction = direction
        self.color = color
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        print(self.direction + " " + self.color + " - ON")
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        print(self.direction + " " + self.color + " - OFF")
        GPIO.output(self.pin,GPIO.LOW)

class Button:
    Pressed = False

    def __init__(self):
        self.pin = 7
        GPIO.setup(self.pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    def press(self):
        input_state = GPIO.input(self.pin)
        if input_state == False:
            print("Button - Pressed")
            self.Pressed = True

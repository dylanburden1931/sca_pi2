#!/usr/bin/env python  
import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO . setmode (GPIO.BOARD)
GPIO . setwarnings (False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

#set passive Buzzers pin's mode as output
GPIO . setup (buzz_pin , GPIO . OUT)

# create buzz function and set initial sound frequency to 1000 hz
Buzz = GPIO . PWM (buzz_pin , 1000)
Buzz . ChangeFrequency (400)

#start passive buzzer using buzz function with 50% duty for 1second 
Buzz.start (50)
time.sleep (1)

# stop Passive Buzzer using Buzz Function
Buzz.stop ()

#reset GPIO resources used by script
GPIO . cleanup ()

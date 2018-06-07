#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO . setmode(GPIO . BOARD)
GPIO . setwarnings(False)

#assign pin number for Touch Switch; pin 31 = GPIO 6
touch_pin = 31
led_pin = 11

#set touch switch pin's mode as input
GPIO . setup(touch_pin , GPIO . IN)
GPIO . setup(led_pin, GPIO . OUT)

# create infinite loop that reads touch switch input
while True:
    if GPIO . input(touch_pin) == 0:
        GPIO . output(led_pin, True)
    if GPIO . input(touch_pin) == 1:
        GPIO . output(led_pin, False)

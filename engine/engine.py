#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import servo as Servo
import time
import signal
import sys

def exit_handler(signal, frame):
    print("\nExit")
    servo.stop()
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

servo = Servo()

while True:
    if GPIO.input(21) == 0:
        servo.action()

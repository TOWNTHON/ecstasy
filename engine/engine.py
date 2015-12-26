#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
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

GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

servo = GPIO.PWM(18, 50)
servo.start(0.0)

dc = 0.0

while True:

    if GPIO.input(21) == 0:
        for dc in range(2, 12, 1):
            servo.ChangeDutyCycle(dc)
            print("dc = %d" % dc)
            time.sleep(0.05)

        for dc in range(12, 2, -1):
            servo.ChangeDutyCycle(dc)
            print("dc = %d" % dc)
            time.sleep(0.05)

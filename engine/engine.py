#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import servo as Servo
import water_sensor as WaterSensor
import signal
import sys

def exit_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)


GPIO.setmode(GPIO.BCM)

servo = Servo()
water_sensor = WaterSensor()

while True:
    if water_sensor.is_wet():
        servo.action()

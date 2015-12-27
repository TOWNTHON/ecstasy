#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class Servo:
    PORT = 18

    def __init__(self):
        GPIO.setup(PORT, GPIO.OUT)

        self.output = GPIO.PWM(PORT, 50)
        self.output.start(0.0)

    def action(self):
        for dc in range(2, 12, 1):
            self.output.ChangeDutyCycle(dc)
            time.sleep(0.05)

        for dc in range(12, 2, -1):
            self.output.ChangeDutyCycle(dc)
            time.sleep(0.05)

    def __del__(self):
        self.output.stop()

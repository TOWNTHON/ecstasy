#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

class WaterSensor:
    PORT = 21

    def __init__(self):
        GPIO.setup(PORT, GPIO.IN)

    def is_wet(self):
        return GPIO.input(PORT) == 0

    def __del__(self):
        pass

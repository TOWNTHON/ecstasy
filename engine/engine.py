#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from servo import Servo
from buzzer import Buzzer
from water_sensor import WaterSensor

class Engine:
    # コンストラクタ
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.water_sensor = WaterSensor()

        self.servo = Servo()
        self.buzzer = Buzzer()

    # エンジンを起動する
    def run(self):
        while True:
            self.__cycle()

    # 1ループごとの処理
    def __cycle(self):
        if self.water_sensor.is_wet():
            self.servo.action()

            if not self.buzzer.is_playing:
                self.buzzer.play()

    # デストラクタ
    def __del__(self):
        GPIO.cleanup()

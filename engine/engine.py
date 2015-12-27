#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import servo as Servo
import water_sensor as WaterSensor

class Engine:
    # コンストラクタ
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.servo = Servo()
        self.water_sensor = WaterSensor()

    # エンジンを起動する
    def run(self):
        while True:
            __cycle()

    # 1ループごとの処理
    def __cycle(self):
        if water_sensor.is_wet():
            servo.action()

    # デストラクタ
    def __del__(self):
        GPIO.cleanup()

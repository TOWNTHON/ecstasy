#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# サーボ制御用クラス
class Servo:
    # GPIOポート番号
    PORT = 18

    # コンストラクタ
    def __init__(self):
        GPIO.setup(PORT, GPIO.OUT)

        self.output = GPIO.PWM(PORT, 50)
        self.output.start(0.0)

    # サーボを動かす
    def action(self):
        for dc in range(2, 12, 1):
            self.output.ChangeDutyCycle(dc)
            time.sleep(0.05)

        for dc in range(12, 2, -1):
            self.output.ChangeDutyCycle(dc)
            time.sleep(0.05)

    # デストラクタ
    def __del__(self):
        self.output.stop()

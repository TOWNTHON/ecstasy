#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# スピーカー制御用クラス
class Buzzer:
    # GPIOポート番号
    PORT = 20

    # コンストラクタ
    def __init__(self):
        GPIO.setup(Buzzer.PORT, GPIO.OUT)
        self.output = GPIO.PWM(Buzzer.PORT, 1000)

    def play(self):
        self.output.start(50) # start BZ1 duty 50%
        time.sleep(5)

        self.output.ChangeFrequency(500) # change frequency 500 Hz
        time.sleep(5)

        self.output.ChangeFrequency(500) # change frequency 500 Hz
        time.sleep(5)

        self.output.ChangeDutyCycle(10) # change duty cycle 10 %
        time.sleep(5)

        self.output.stop() # stop self.output

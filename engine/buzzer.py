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
        GPIO.setup(Speaker.PORT, GPIO.OUT)
        self.output = GPIO.PWM(BZ1, 1000)

    def play(self):
        buzzer.start(50) # start BZ1 duty 50%
        time.sleep(5)

        buzzer.ChangeFrequency(500) # change frequency 500 Hz
        time.sleep(5)

        buzzer.ChangeFrequency(500) # change frequency 500 Hz
        time.sleep(5)

        buzzer.ChangeDutyCycle(10) # change duty cycle 10 %
        time.sleep(5)

        buzzer.stop() # stop buzzer

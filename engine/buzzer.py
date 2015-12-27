#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# スピーカー制御用クラス
class Buzzer:
    # GPIOポート番号
    PORT = 20

    DOREMI = [220.0, 246.9, 277.2, 293.7, 329.6, 370.0, 415.3, 440.0]

    # コンストラクタ
    def __init__(self):
        GPIO.setup(Buzzer.PORT, GPIO.OUT)
        self.output = GPIO.PWM(Buzzer.PORT, 1000)

    def play(self):
        self.output.start(50)

        for freq in Buzzer.DOREMI:
            self.output.ChangeFrequency(freq)
            time.sleep(1)

        self.output.stop()

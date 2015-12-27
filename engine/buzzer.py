#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import chart.scale as Scale 
import time

# スピーカー制御用クラス
class Buzzer:
    # GPIOポート番号
    PORT = 20

    CHART = [
        (Scale.C1, 3),
        (Scale.D1, 1),
        (Scale.E1, 3),
        (Scale.C1, 1),
        (Scale.E1, 2),
        (Scale.C1, 2),
        (Scale.E1, 4),
        ]

    # コンストラクタ
    def __init__(self):
        GPIO.setup(Buzzer.PORT, GPIO.OUT)
        self.output = GPIO.PWM(Buzzer.PORT, 1000)

    def play(self):
        self.output.start(50)

        for note in Buzzer.CHART:
            self.output.ChangeFrequency(Scale.SCALE[note[0]])
            time.sleep(note[1]/3.0)

        self.output.stop()

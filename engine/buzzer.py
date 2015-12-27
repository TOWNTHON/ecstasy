#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# スピーカー制御用クラス
class Buzzer:
    # GPIOポート番号
    PORT = 20

    SCALE = {
            "C1": 220.0,
            "D1": 246.9,
            "E1": 277.2,
            "F1": 293.7,
            "G1":329.6,
            "A1":370.0,
            "B1":415.3,
            "C2":440.0
            }

    CHART = [
        ("C1", 3),
        ("D1", 1),
        ("E1", 3),
        ("C1", 1),
        ("E1", 2),
        ("C1", 2),
        ("E1", 5),
        ]

    # コンストラクタ
    def __init__(self):
        GPIO.setup(Buzzer.PORT, GPIO.OUT)
        self.output = GPIO.PWM(Buzzer.PORT, 1000)

    def play(self):
        self.output.start(50)

        for note in Buzzer.CHART:
            self.output.ChangeFrequency(Buzzer.SCALE[note[0]])
            time.sleep(note[1])

        self.output.stop()

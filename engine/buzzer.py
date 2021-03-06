#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import chart.scale as Scale
import chart.strawberry_sex as StrawberrySex
import time
import threading

# スピーカー制御用クラス
class Buzzer:
    # GPIOポート番号
    PORT = 20

    # コンストラクタ
    def __init__(self):
        GPIO.setup(Buzzer.PORT, GPIO.OUT)
        self.output = GPIO.PWM(Buzzer.PORT, 1000)

        self.thread = None

    # 音楽を再生する
    def play(self):
        self.thread = threading.Thread(target=self._play, name="thread")
        self.thread.start()

    # 音楽が再生中かどうか調べる
    def is_playing(self):
        return self.thread is not None and self.thread.is_alive()

    def _play(self):
        for note in StrawberrySex.CHART:
            freq = note[0]

            if not freq == Scale.REST:
                self.output.start(50)
                self.output.ChangeFrequency(Scale.SCALE[freq])

            time.sleep(note[1]/5.0)

            if not freq == Scale.REST:
                self.output.stop()

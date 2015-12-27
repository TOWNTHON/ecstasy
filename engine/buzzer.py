#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import chart.scale as Scale
import chart.doremi as Doremi
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

    # 音楽を再生する
    def play(self):
        self.thread = threading.Thread(target=self._play, name="thread")
        self.thread.start()

    # 音楽が再生中かどうか調べる
    def is_playing(self):
        return self.thread is not None and self.thread.is_alive()

    def _play(self):
        self.output.start(50)

        for note in Doremi.CHART:
            self.output.ChangeFrequency(Scale.SCALE[note[0]])
            time.sleep(note[1]/3.0)

        self.output.stop()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

# 水センサ制御用クラス
class WaterSensor:
    # GPIOポート番号
    PORT = 21

    # コンストラクタ
    def __init__(self):
        GPIO.setup(PORT, GPIO.IN)

    # センサーが水に濡れているかどうかを調べる
    def is_wet(self):
        return GPIO.input(PORT) == 0

    # デストラクタ
    def __del__(self):
        pass

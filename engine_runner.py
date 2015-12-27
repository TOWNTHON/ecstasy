#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal
import sys
from engine.engine import Engine

# エンジン終了処理
def exit_handler(signal, frame):
  print("\nExit")
  sys.exit(0)
signal.signal(signal.SIGINT, exit_handler)

engine = Engine()
engine.run()

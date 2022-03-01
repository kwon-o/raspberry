#!/usr/bin/env python3
"""
RPZ-IR-Sensor サンプルプログラム

1) ターミナルを開き、本ファイルと同じディレクトリで以下の$に続くコマンドを実行します
  $ ./rpzir_ledsw.py

2) 赤スイッチ、黒スイッチを押すとLEDの色が変わります
  赤スイッチが押されている: LED1(緑)とLED2(黄)が点灯
  黒スイッチが押されている: LED3(青)とLED4(白)が点灯
  両方押されている: 全てのLEDが点灯
  両方おされていない: 全てのLEDが消灯

3) キーボードからCtrl+Cを入力すると終了します
"""

import time
import RPi.GPIO as GPIO

LED1 = 17  # 緑色LED GPIO番号
LED2 = 18  # 黄色LED GPIO番号
LED3 = 22  # 青色LED GPIO番号
LED4 = 27  # 白色LED GPIO番号
SW1 = 5  # 赤スイッチのGPIO番号
SW2 = 6  # 黒スイッチのGPIO番号

print('RPZ-IR-Sensor サンプルプログラム')

# GPIOの準備
GPIO.setmode(GPIO.BCM)

# RGB LEDピン出力設定
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

# SW1, SW2ピン入力設定
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time.sleep(0.01)

print('赤、黒スイッチを押すとLEDの色が変わります')
print('Ctrl+Cで終了します')

try:
  # 無限ループ
  while True:
    if 0 == GPIO.input(SW1):
      GPIO.output(LED1, 1)  # 赤スイッチが押されたら緑色LED ON
      GPIO.output(LED2, 1)  # 赤スイッチが押されたら黄色LED ON
    else:
      GPIO.output(LED1, 0)  # 赤スイッチが押されていなければ緑色LED OFF
      GPIO.output(LED2, 0)  # 赤スイッチが押されていなければ黄色LED OFF

    if 0 == GPIO.input(SW2):
      GPIO.output(LED3, 1)  # 黒スイッチが押されたら青色LED ON
      GPIO.output(LED4, 1)  # 黒スイッチが押されたら白色LED ON
    else:
      GPIO.output(LED3, 0)  # 黒スイッチが押されていなければ青色LED OFF
      GPIO.output(LED4, 0)  # 黒スイッチが押されていなければ白色LED OFF

    time.sleep(0.01)  # 待機

except KeyboardInterrupt:
  # Ctrl+Cが押されたら後片付けをして終了
  GPIO.output(LED1, 0)
  GPIO.output(LED2, 0)
  GPIO.output(LED3, 0)
  GPIO.output(LED4, 0)
  GPIO.cleanup()

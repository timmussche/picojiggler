# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Example for Pico. Turns on the built-in LED."""
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep
m = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    m.move(-100, 0, 0)
    print("I am working")
    sleep(0.5)
    led.value = False
    m.move(100, 0, 0)
    print("I am so busy")
    sleep(0.5)
    led.value = True
    m.move(0, -100, 0)
    print("So much to do")
    sleep(0.5)
    led.value = False
    m.move(0, 100, 0)
    print("I need a vacation")
    sleep(0.5)
# Macropad

In this repo you find some useful (maybe) info about how to turn your raspberry pi pico into macropad

# Hardware

1x RPi Pico
Nx Buttons
1x Micro USB cable
1x 3d printer (for cool case)
Few wires

# Preparation

First of all, you should flash right firmware. For this project I will use [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)

## Firmware

To flash firmware:

1. Unplug USB cable from RPi pico
2. Press BOOTSEL button and hold it
3. Plug in USB cable into RPi pico
4. Your RPi should appears on PC as a usual drive
5. Copy CuircuitPython .uf2 file into this RPi drive. It will install it and reboot automatically. After that, your RPi is good to go

## Libs

To allow our RPi communicate with PC and emulate USB HID device, we need additional library. For example, I will use [Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID)

Download latest release from there and unpack lib folder into lib folder on raspberry pi

# Software

You can use [Thonny IDE](https://thonny.org/) to connect to RPi pico and code

Create main.py on your RPi pico or copy main.py from this repo to your RPi pico and that's it. Your RPi is now macropad with buttons F13-F24

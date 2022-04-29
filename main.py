import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP4
btn2_pin = board.GP5
btn3_pin = board.GP6
btn4_pin = board.GP7
btn5_pin = board.GP8
btn6_pin = board.GP9
btn7_pin = board.GP10
btn8_pin = board.GP11
btn9_pin = board.GP12
btn10_pin = board.GP13
btn11_pin = board.GP14
btn12_pin = board.GP15

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print('Btn1 pressed')
        keyboard.press(Keycode.F13)
        time.sleep(0.1)
        keyboard.release(Keycode.F13)
    if btn2.value:
        print('Btn2 pressed')
        keyboard.press(Keycode.F14)
        time.sleep(0.1)
        keyboard.release(Keycode.F14)
    if btn3.value:
        print('Btn3 pressed')
        keyboard.press(Keycode.F15)
        time.sleep(0.1)
        keyboard.release(Keycode.F15)
    if btn4.value:
        print('Btn4 pressed')
        keyboard.press(Keycode.F16)
        time.sleep(0.1)
        keyboard.release(Keycode.F16)
    if btn5.value:
        print('Btn5 pressed')
        keyboard.press(Keycode.F17)
        time.sleep(0.1)
        keyboard.release(Keycode.F17)
    if btn6.value:
        print('Btn6 pressed')
        keyboard.press(Keycode.F18)
        time.sleep(0.1)
        keyboard.release(Keycode.F18)
    if btn7.value:
        print('Btn7 pressed')
        keyboard.press(Keycode.F19)
        time.sleep(0.1)
        keyboard.release(Keycode.F19)
    if btn8.value:
        print('Btn8 pressed')
        keyboard.press(Keycode.F20)
        time.sleep(0.1)
        keyboard.release(Keycode.F20)
    if btn9.value:
        print('Btn9 pressed')
        keyboard.press(Keycode.F21)
        time.sleep(0.1)
        keyboard.release(Keycode.F21)
    if btn10.value:
        print('Btn10 pressed')
        keyboard.press(Keycode.F22)
        time.sleep(0.1)
        keyboard.release(Keycode.F22)
    if btn11.value:
        print('Btn11 pressed')
        keyboard.press(Keycode.F23)
        time.sleep(0.1)
        keyboard.release(Keycode.F23)
    if btn12.value:
        print('Btn12 pressed')
        keyboard.press(Keycode.F24)
        time.sleep(0.1)
        keyboard.release(Keycode.F24)
    time.sleep(0.1)



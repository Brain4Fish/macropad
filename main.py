import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


class Btn:
    def __init__(self, pin, code):
        self.pin = pin
        self.code = code
        self.btn = None
    
    def init_btn(self):
        self.btn = digitalio.DigitalInOut(self.pin)
        self.btn.direction = digitalio.Direction.INPUT
        self.btn.pull = digitalio.Pull.DOWN


keyboard = Keyboard(usb_hid.devices)

btn_lst = [
    Btn(board.GP4,  Keycode.F13),
    Btn(board.GP5,  Keycode.F14),
    Btn(board.GP6,  Keycode.F15),
    Btn(board.GP7,  Keycode.F16),
    Btn(board.GP8,  Keycode.F17),
    Btn(board.GP9,  Keycode.F18),
    Btn(board.GP10, Keycode.F19),
    Btn(board.GP11, Keycode.F20),
    Btn(board.GP12, Keycode.F21),
    Btn(board.GP13, Keycode.F22),
    Btn(board.GP14, Keycode.F23),
    Btn(board.GP15, Keycode.F24),
]

for btn in btn_lst: 
    btn.init_btn()


while True:
    for btn in btn_lst: 
        if btn.btn.value:
            keyboard.press(btn.code)
            time.sleep(0.1)
            keyboard.release(btn.code)

    time.sleep(0.1)

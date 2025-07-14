from pynput import mouse
from time import time

class mouse_controller:
    def __init__(self):
        self.controller = mouse.Controller()
        self.button_state = 0
        self.button_timer = 0

    def button_hold(self, button):
        if self.button_state < 1:
            self.controller.press(button)
            self.button_state = 1
            print(f'Hold {button.name} button')
        else:
            self.controller.release(button)
            self.button_state = 0
            print(f'Released {button.name} button')

    def set_button_time(self, button_time):
        self.button_timer = button_time

    def get_button_time(self):
        return self.button_timer


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        c.set_button_time(int(time()*1000))
    elif button == mouse.Button.left and not pressed:
        if int(time()*1000) - c.get_button_time() > 800:
            c.button_hold(button)


c = mouse_controller()
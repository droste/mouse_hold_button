from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print(f'left')
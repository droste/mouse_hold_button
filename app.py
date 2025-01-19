from pynput import mouse
from mouse.mouse import on_click


if __name__ == "__main__":
    with mouse.Listener(
        on_click=on_click
    ) as listener:
        listener.join()

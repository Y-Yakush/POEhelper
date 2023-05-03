from pynput import keyboard
from script import active_elements_search


def start_script(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.GlobalHotKeys({'<ctrl>+<alt>+y': active_elements_search}) as strt:
    strt.join()


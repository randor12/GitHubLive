##
# Ryan Nicholas
# Auto Save Code

import pyautogui
import time


def autoSave():
    pyautogui.hotkey('ctrl', 's')


def main():
    for i in range(2000):
        if i % 20 == 0:
            autoSave()
            print("Saved")
        else:
            print("Saving")
    time.sleep(.1)


main()

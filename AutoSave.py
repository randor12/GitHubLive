##
# Ryan Nicholas
# Auto Save Code

import os
import time


def getFile():
    folder = input("Input repository path: ")
    return folder


def autoSave(folder):
    files = os.listdir(folder)
    print(files)
    for f in files:
        badFile = f.__contains__(".git") or f.__contains__("README")
        if not badFile:
            save = open(f)
            save.close()


def main():
    folder = getFile()
    for i in range(2000):
        autoSave(folder)
        print("Saved")
        time.sleep(.1)


main()

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
        goodFile = f.__contains__(".")
        if not badFile and goodFile:
            save = open(folder + f, 'a')
            if save.readable():
                print(save.readlines())
            save.close()


def main():
    folder = getFile()
    autoSave(folder)
    print("Saved")
    time.sleep(.1)


main()

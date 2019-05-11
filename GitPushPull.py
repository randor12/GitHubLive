##
# Ryan Nicholas
# Make the automatic git push/pull

import os
import keyboard
from git import Repo

path = input("Input the repo path: ")

repo = Repo(path)

while True:
    try:
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("s"):
            fileList = os.listdir(path)
            commitMessage = "Changed code"
            repo.index.add(fileList)
            repo.index.commit(commitMessage)
            origin = repo.remote('origin')
            origin.push()
            origin.pull()
            print("Changed!")
        elif keyboard.is_pressed("ctrl") and keyboard.is_pressed("q"):
            break
        else:
            pass
    except:
        break

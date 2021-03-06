##
# Ryan Nicholas
# Make the automatic git push/pull

import os
import keyboard
from git import Repo

path = input("Input the repo path: ")

while True:
    try:
        repo = Repo(path)
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("s"):
            print("Changing")
            fileList = os.listdir(path)
            actualFiles = []
            for file in fileList:
                if not file.__contains__(".git") and not file.__contains__("README"):
                    actualFiles.append(file)
            commitMessage = "Changed code"
            repo.index.add(actualFiles)
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

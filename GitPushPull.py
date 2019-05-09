##
# Ryan Nicholas
# Make the automatic git push/pull

import os
import keyboard
import time
import git

c = True

path = input("Input the repo path: ")

while c:
    try:
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("s"):
            file = os.listdir(path)
            for f in file:
                goodFile = f.__contains__(".")
                if goodFile:
                    git.Remote.add(path + f)
            git.Repo.commit(repo)
            git.Remote.push(repo)
            git.Remote.pull(repo)
        elif keyboard.is_pressed("ctrl") and keyboard.is_pressed("q"):
            c = False
        else:
            pass
    except:
        break
    time.sleep(.05)


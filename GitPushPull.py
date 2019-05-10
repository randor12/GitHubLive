##
# Ryan Nicholas
# Make the automatic git push/pull

import os
import keyboard
import time
import git

path = input("Input the repo path: ")

repo = git.Repo(path)
remote = git.Repo.remote(repo)

while True:
    try:
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("s"):
            file = os.listdir(path)
            for f in file:
                goodFile = f.__contains__(".")
                if goodFile:
                    git.Remote.add(path + f)
            git.Repo.commit(repo)
            git.Remote.push(remote)
            git.Remote.pull(remote)
        elif keyboard.is_pressed("ctrl") and keyboard.is_pressed("q"):
            break
        else:
            pass
    except:
        break
    time.sleep(.05)

#!/usr/bin/python

import datetime
import os
import subprocess
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

class Handler(FileSystemEventHandler):

    def __init__(self, time = datetime.datetime.now()):
        self.time = time

    def on_modified(self, event):
        time.sleep(1)
        os.system("cls")
        print(event.src_path)
        if event.src_path == r'.\Wars.py':
            print("called")
            if is_non_zero_file(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))),
                                                "wars.py",
                                            )):
                print("\n")
                print("Output: ")
                print("\n")
                subprocess.run(["python", event.src_path])
            else:
                open(
                    os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "notes.txt",
                                ),
                    "w",
                    ).close()
                os.system("cls")

if __name__ == "__main__":
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path = ".", recursive = False)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

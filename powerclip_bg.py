"""Background task constantly verifying there is no new clipboard content"""
import time
import os
import json

import pystray
from pynput import keyboard

import powerclip_gui

def refresh():
    """Save changes to and reload json file"""
    with open('clips.json', 'r') as clips:
        try:
            currentClipboardContent = json.load(clips)
        except Exception:
            print('Clipboard is empty')
            currentClipboardContent = []

    print("old", currentClipboardContent)

    newClipboardContent = os.popen("xsel -ob").read()
    print("new", newClipboardContent)
    if newClipboardContent not in currentClipboardContent:
        print('Appending...')
        currentClipboardContent.append(newClipboardContent)
        with open('clips.json', 'w') as newFile:
            json.dump(currentClipboardContent, newFile)


def open_gui():
    """Save changes to clips.json and run GUI"""
    refresh()
    exec(open('powerclip_gui.py').read())

COMBINATION = {keyboard.Key.cmd, keyboard.KeyCode.from_char('v')}
current = set()


def on_press(key):
    """Handling key presses"""
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print("Opening GUI ...")
            open_gui()


def on_release(key):
    """Handling key releases"""
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

while True:
    refresh()
    time.sleep(0.5)

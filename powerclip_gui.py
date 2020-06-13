"Run the powerclip gui"
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import pyperclip
import os
import json

def set_current_entry(entry):
    """Changes the current clipboard entry to match `entry`"""
    print(f"Entry {entry.text()} set as current")


def gui():
    """Loads the json, runs the Qt GUI
    Returns the modified clipboardContent list"""
    with open('clips.json', 'r') as clips:
        clipboardContent = json.load(clips)

    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    for i in clipboardContent:
        clipboardEntry = QPushButton(i)
        clipboardEntry.clicked.connect(lambda:set_current_entry(clipboardEntry))
        layout.addWidget(clipboardEntry)

    window.setLayout(layout)
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    window.show()

    print('Powerclip GUI started.')
    app.exec_()
    print('Powerclip GUI stopped.')
    return clipboardContent


postGUIClipboardContent = gui()
print('Updated clipboard content: \n', postGUIClipboardContent)
with open('clips.json', 'w') as newFile:
    json.dump(postGUIClipboardContent, newFile)


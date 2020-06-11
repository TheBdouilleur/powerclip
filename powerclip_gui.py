"Run the powerclip gui"
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import pyperclip
import os
import json

def gui():
    with open('clips.json', 'r') as clips:
        clipboardContent = json.load(clips)

    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    for i in clipboardContent:
        layout.addWidget(QPushButton(i))

    window.setLayout(layout)
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    window.show()
    app.exec_()
    print('Powerclip GUI started.')


gui()

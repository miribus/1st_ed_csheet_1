# Filename: f_layout.py

"""Form layout example."""

import character_gui, sys
from PyQt5.QtWidgets import *
rollchoices = character_gui.rollchoices

rchoice = ""
rollc = ""
def on_button_clicked():
    global rchoice, rollc
    print(rchoice, rollc)

def rollbuttons():
    global rchoice, rollc
    btns = {}
    for c in character_gui.rollchoices:
        btns[c] = QPushButton(character_gui.rollchoices[c])

        #print(rollc)
    for c in btns:
        rollc = c
        btns[c].clicked.connect(on_button_clicked)
        layout.addWidget(btns[c])
        #rollc = c
        #rollc.clicked.connect(on_button_clicked)

    #return layout


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('1E AD&D 1985 Character Generator')
layout = QFormLayout()
#layout =
rollbuttons()
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
'''
button = QPushButton('Click')
button2 = QPushButton('Click2')
layout.addRow(button, QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job:', QLineEdit())
layout.addRow('Hobbies:', QLineEdit())

button.clicked.connect(on_button_clicked)
'''

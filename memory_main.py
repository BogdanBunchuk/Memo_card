from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
app = QApplication([])
from memory_layout import *


def click_OK(self):
    if submit.text() != 'Следущий вопрос':
        check_result()
    elif submit.text() != 'Ответить':
        show_question()


def click_menu(self):
    win_card.hide()
    win_custom.show()

def click_back(self):
    win_card.show()
    win_custom.hide()
    
win_height, win_weight = 500, 600
win_card = QWidget()
win_card.resize(win_weight, win_height)
win_card.setWindowTitle('Memory Card')
win_card.move(300, 300)
win_card.show()

layout_card = QVBoxLayout()
layout_card.stretch(2)
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)
show_question()
submit.clicked.connect(click_OK)
menu_button.clicked.connect(click_menu)
back.clicked.connect(click_back)
win_card.setLayout(layout_card)

app.exec_()
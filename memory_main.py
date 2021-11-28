from PyQt5.QtCore import QTimer, qWarning
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication([])
from memory_layout import *

def click_OK(self):
    if submit.text() != 'Следущий вопрос':
        check_result()
    elif submit.text() != 'Ответить':
        show_question()

def sleep_click(self):
    not_working.show()


def click_edit_button(self):
    welcome_text.setText('Тестирвание знаний')
    main_win.hide()
    win_custom.show()

def click_test_button(self):
    welcome_text.setText('Тестирвание знаний')
    main_win.hide()
    win_card.show()

def click_menu(self):
    win_card.hide()
    main_win.show()

def click_back(self):
    main_win.show()
    win_custom.hide()
    
def ok_click(self):
    not_working.hide()

main_win = QWidget()
main_win.resize(300, 300)
main_win.move(800, 300)
main_win.setWindowTitle('Memory Card Menu')
welcome_text = QLabel('Добро пожаловать!')
edit_button = QPushButton('Редактор вопросов')
test_button = QPushButton('Начать тестирование')
welcome_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()
buttons_layout.addWidget(edit_button)
buttons_layout.addWidget(test_button)
welcome_layout.addWidget(welcome_text, alignment = Qt.AlignCenter)
welcome_layout.addLayout(buttons_layout)
main_win.setLayout(welcome_layout)
main_win.show()

not_working = QWidget()
not_working_text = QLabel('копка временно не работает, когда-то починем')
not_working_line = QVBoxLayout()
not_working.resize(500, 200)
not_working.move(500, 500)
not_working.setWindowTitle('error')
not_working_line.addWidget(not_working_text)
ok_button = QPushButton('ok')
not_working_line.addWidget(ok_button)
not_working.setLayout(not_working_line)

win_height, win_weight = 500, 600
win_card = QWidget()
win_card.resize(win_weight, win_height)
win_card.setWindowTitle('Memory Card')
win_card.move(300, 300)

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
edit_button.clicked.connect(click_edit_button)
test_button.clicked.connect(click_test_button)
sleep.clicked.connect(sleep_click)
ok_button.clicked.connect(ok_click)
win_card.setLayout(layout_card)

app.exec_()
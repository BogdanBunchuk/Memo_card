from PyQt5.QtCore import QTimer, qWarning
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication([])
from memory_layout import *
import time

def click_OK(self):
    if submit.text() != 'Следущий вопрос':
        check_result()
    elif submit.text() != 'Ответить':
        show_question()

def sleep_click(self):
    bm_time = int(box_minutes.value())
    local_time = float(bm_time)
    local_time *= 60
    win_card.hide()
    time.sleep(local_time)
    win_card.show()
    
def click_test_button(self):
    welcome_text.setText('Тестирвание знаний')
    main_win.hide()
    win_card.show()

def click_menu(self):
    win_card.hide()
    main_win.show()


main_win = QWidget()
main_win.resize(300, 300)
main_win.move(800, 300)
main_win.setWindowTitle('Memory Card Menu')
welcome_text = QLabel('Добро пожаловать!')
edit_button = QPushButton('Редактор вопросов')
test_button = QPushButton('Начать тестирование')
welcome_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()
buttons_layout.addWidget(test_button)
welcome_layout.addWidget(welcome_text, alignment = Qt.AlignCenter)
welcome_layout.addLayout(buttons_layout)
main_win.setLayout(welcome_layout)
main_win.show()


win_height, win_weight = 500, 600
win_card = QWidget()
win_card.resize(win_weight, win_height)
win_card.setWindowTitle('Memory Card')
win_card.move(300, 300)

edit_button.hide()

layout_card = QVBoxLayout()
layout_card.stretch(2)
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)
show_question()
submit.clicked.connect(click_OK)
menu_button.clicked.connect(click_menu)
test_button.clicked.connect(click_test_button)
sleep.clicked.connect(sleep_click)
win_card.setLayout(layout_card)

app.exec_()
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
app = QApplication([])
from memory_layout import *

def show_data():
    lb_Quesion.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    correct = answer.isChecked()
    if correct:
        lb_Result.setText('Верно')
        show_result()
    incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
    if incorrect:
        lb_Result.setText('Неверно')
        show_result()


def click_OK(self):
    if submit.text() != 'Наступний':
        check_result()

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
show_data()
show_question()
submit.clicked.connect(click_OK)
win_card.setLayout(layout_card)

app.exec_()
from typing import Counter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from memory_custom import *
import random
menu_button = QPushButton('Меню')
sleep = QPushButton('Отдохнуть')
box_minutes = QSpinBox()
box_minutes.setValue(30)
text = QLabel('Минут')

counter = QLabel('0')
result_count = QLabel('Верно. Всего отвечено верно 0/4')

question = QLabel('')

RadioGroupBox = QGroupBox('Варианты ответа')
RadioGroup = QButtonGroup()

RadButton1 = QRadioButton('')
RadButton2 = QRadioButton('')
RadButton3 = QRadioButton('')
RadButton4 = QRadioButton('')

RButton_group = [RadButton1, RadButton2, RadButton3, RadButton4]
random.shuffle(RButton_group)

RadioGroup.addButton(RButton_group[0])
RadioGroup.addButton(RButton_group[1])
RadioGroup.addButton(RButton_group[2])
RadioGroup.addButton(RButton_group[3])

answer1 = RButton_group[0]
answer2 = RButton_group[1]
answer3 = RButton_group[2]
answer4 = RButton_group[3]

submit = QPushButton('Ответить')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(answer1)
layout_ans2.addWidget(answer2)
layout_ans3.addWidget(answer3)
layout_ans3.addWidget(answer4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

text_correct = 'Верно'
text_wrong = 'Неверно'

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('')
correct_ans = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(result_count, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct_ans, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()



layout_test = QHBoxLayout()

layout_line1 = QHBoxLayout()
layout_line2 = QVBoxLayout()
layout_line3 = QVBoxLayout()
layout_line4 = QVBoxLayout()

layout_line1.addWidget(menu_button, alignment = Qt.AlignLeft)
layout_test.addStretch(1)
layout_test.addWidget(sleep, alignment = Qt.AlignRight)
layout_test.addWidget(box_minutes, alignment = Qt.AlignRight)
layout_test.addWidget(text, alignment = Qt.AlignRight)
layout_line1.addLayout(layout_test)
layout_line2.addWidget(question, alignment = Qt.AlignCenter)
RadioGroupBox.setLayout(layout_ans1)
layout_line3.addWidget(RadioGroupBox, stretch=2)
layout_line3.addWidget(AnsGroupBox, stretch=2)
layout_line4.addWidget(submit, stretch=2)

class Question():
    def __init__(self, question, correct, answer1, answer2, answer3, answer4):
        self.question = question
        self.correct = correct
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
    def set_question(self):
        question.setText(self.question)
        correct_ans.setText(self.correct)
        answer1.setText(self.answer1)
        answer2.setText(self.answer2)
        answer3.setText(self.answer3)
        answer4.setText(self.answer4)
    
    def got_right(self):
        print('Это правиьный ответ!')
    def got_wrong(self):
        print('Ответ неверный')


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    submit.setText('Следущий вопрос')

def check_result():
    if counter.text() == '1':
        correct = answer4.isChecked()
        incorrect = answer1.isChecked() or answer2.isChecked() or answer3.isChecked()
    elif counter.text() == '2':
        correct = answer3.isChecked()
        incorrect = answer4.isChecked() or answer2.isChecked() or answer1.isChecked()
    elif counter.text() == '3':
        correct = answer1.isChecked()
        incorrect = answer4.isChecked() or answer2.isChecked() or answer3.isChecked()
    elif counter.text() == '4':
        correct = answer4.isChecked()
        incorrect = answer1.isChecked() or answer2.isChecked() or answer3.isChecked()
        question.setText('Тест закончен. Выйдите из программы')
        submit.hide()

    if correct:
        if '0' in result_count.text():
            result_count.setText('Верно. Всего отвечено верно 1/4')
        elif '1' in result_count.text():
            result_count.setText('Верно. Всего отвечено верно 2/4')
        elif '2' in result_count.text():
            result_count.setText('Верно. Всего отвечено верно 3/4')
        elif '3' in result_count.text():
            result_count.setText('Верно. Всего отвечено верно 4/4')

        show_result()
    if incorrect:

        if '0' in result_count.text():
            result_count.setText('Неверно. Всего отвечено верно 0/4')
        elif '1' in result_count.text():
            result_count.setText('Неверно. Всего отвечено верно 1/4')
        elif '2' in result_count.text():
            result_count.setText('Неверно. Всего отвечено верно 2/4')
        elif '3' in result_count.text():
            result_count.setText('Неверно. Всего отвечено верно 3/4')
        show_result()



def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    submit.setText('Ответить')

    RadioGroup.setExclusive(False)#Зняти обмеження, щоб скинути вибір
    RadButton1.setChecked(False)
    RadButton2.setChecked(False)
    RadButton3.setChecked(False)
    RadButton4.setChecked(False)
    RadioGroup.setExclusive(True)
    if counter.text() == '0':
        q1 = Question(ques1[0], ques1[4], ques1[1], ques1[2], ques1[3], ques1[4])
        counter.setText('1')
    elif counter.text() == '1':
        q1 = Question(ques2[0], ques2[1], ques2[1], ques2[2], ques2[3], ques2[4])
        counter.setText('2')
    elif counter.text() == '2':
        q1 = Question(ques3[0], ques3[1], ques3[1], ques3[2], ques3[3], ques3[4])
        counter.setText('3')
    elif counter.text() == '3':
        q1 = Question(ques4[0], ques4[4], ques4[1], ques4[2], ques4[3], ques4[4])
        counter.setText('4')
    q1.set_question()
from typing import Counter
from PyQt5.QtWidgets import QPushButton, QRadioButton, QSpinBox, QLabel, QGroupBox, QButtonGroup, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

menu_button = QPushButton('Меню')
sleep = QPushButton('Отдохнуть')
box_minutes = QSpinBox()
box_minutes.setValue(30)
text = QLabel('Минут')

counter = QLabel('0')
result_count = QLabel('Верно. Всего отвечено верно 0/4')

question = QLabel('')
lb_Quesion = QLabel('')

RadioGroupBox = QGroupBox('Варианты ответа')
RadioGroup = QButtonGroup()

RadButton1 = QRadioButton('')
RadButton2 = QRadioButton('')
RadButton3 = QRadioButton('')
RadButton4 = QRadioButton('')

RadioGroup.addButton(RadButton1)
RadioGroup.addButton(RadButton2)
RadioGroup.addButton(RadButton3)
RadioGroup.addButton(RadButton4)

submit = QPushButton('Ответить')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(RadButton1)
layout_ans2.addWidget(RadButton2)
layout_ans3.addWidget(RadButton3)
layout_ans3.addWidget(RadButton4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

text_correct = 'Верно'
text_wrong = 'Неверно'


answer4 = RadButton4
answer1 = RadButton2
answer2 = RadButton3
answer3 = RadButton1


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('') 
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(result_count, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
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

    if correct:
        if result_count.text() == 'Верно. Всего отвечено верно 0/4' or result_count.text() == 'Неверно. Всего отвечено верно 0/4':
            result_count.setText('Верно. Всего отвечено верно 1/4')
        elif result_count.text() == 'Верно. Всего отвечено верно 1/4' or result_count.text() == 'Неверно. Всего отвечено верно 1/4':
            result_count.setText('Верно. Всего отвечено верно 2/4')
        elif result_count.text() == 'Верно. Всего отвечено верно 2/4' or result_count.text() == 'Неверно. Всего отвечено верно 2/4':
            result_count.setText('Верно. Всего отвечено верно 3/4')
        elif result_count.text() == 'Верно. Всего отвечено верно 3/4' or result_count.text() == 'Неверно. Всего отвечено верно 3/4':
            result_count.setText('Верно. Всего отвечено верно 4/4')
            question.setText('Тест закончен. Выйдите из программы')
            submit.hide()
        show_result()
    if incorrect:

        if result_count.text() == 'Верно. Всего отвечено верно 0/4' or result_count.text() == 'Неверно. Всего отвечено верно 0/4':
            result_count.setText('Неверно. Всего отвечено верно 0/4')
        elif result_count.text() == 'Верно. Всего отвечено верно 1/4' or result_count.text() == 'Неверно. Всего отвечено верно 1/4':
            result_count.setText('Неверно. Всего отвечено верно 1/4')
        elif result_count.text() == 'Верно. Всего отвечено верно 2/4' or result_count.text() == 'Неверно. Всего отвечено верно 2/4':
            result_count.setText('Неверно. Всего отвечено верно 2/4')
        elif result_count.text() == 'Верно. Всего отвечено верно 3/4' or result_count.text() == 'Неверно. Всего отвечено верно 3/4':
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
        question.setText('Перевод слова - Яблоко')
        lb_Correct.setText('Apple')
        answer1.setText('Apply')
        answer2.setText('Ant')
        answer3.setText('Appart')
        answer4.setText('Apple')
        counter.setText('1')
    elif counter.text() == '1':
        question.setText('Перевод слова - Piggy bank')
        lb_Correct.setText('Свинья копилка')
        answer1.setText('Банк со свинкой')
        answer2.setText('Банк свиньи')
        answer3.setText('Свинья копилка')
        answer4.setText('Свиной банк')
        counter.setText('2')
    elif counter.text() == '2':
        question.setText('Не являетя правильным переводом - Iron')
        lb_Correct.setText('Мягкий')
        answer1.setText('Мягкий')
        answer2.setText('Утюг')
        answer3.setText('Железный')
        answer4.setText('Железо')
        counter.setText('3')
    elif counter.text() == '3':
        question.setText('Слова, которые не были в вопросах')
        lb_Correct.setText('Твёрдость')
        answer1.setText('Apple')
        answer2.setText('Свинья копилка')
        answer3.setText('Iron')
        answer4.setText('Твёрдость')
        counter.setText('4')
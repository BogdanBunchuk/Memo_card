from PyQt5.QtWidgets import QPushButton, QRadioButton, QSpinBox, QLabel, QGroupBox, QButtonGroup, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

menu_button = QPushButton('Меню')
sleep = QPushButton('Отдохнуть')
box_minutes = QSpinBox()
box_minutes.setValue(30)
text = QLabel('Минут')

question = QLabel('Яблоко')
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
frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'

answer = RadButton4
wrong_answer1 = RadButton2
wrong_answer2 = RadButton3
wrong_answer3 = RadButton1

RadButton1.setText(frm_wrong3)
RadButton2.setText(frm_wrong2)
RadButton3.setText(frm_wrong1)
RadButton4.setText(frm_right)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('') 
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
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
    submit.setText('Наступне питання')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    submit.setText('Відповісти')

    RadioGroup.setExclusive(False)#Зняти обмеження, щоб скинути вибір
    RadButton1.setChecked(False)
    RadButton2.setChecked(False)
    RadButton3.setChecked(False)
    RadButton4.setChecked(False)
    RadioGroup.setExclusive(True)
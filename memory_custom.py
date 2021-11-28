from PyQt5.QtWidgets import *
win_custom = QWidget()
win_custom.resize(900, 400)
win_custom.move(300, 300)
win_custom.setWindowTitle('Редактор вопросов')
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.l = QListWidget()
        self.l.addItems(cus_ques)

        self.l.itemClicked.connect(self.selectionChanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.l)
        self.setLayout(vbox)

    def selectionChanged(self, item):
        if item.text() == cus_ques1[0]:
            if True:
                obj1.setText(cus_ques1[0])
                obj2.setText(cus_ques1[1])
                obj3.setText(cus_ques1[2])
                obj4.setText(cus_ques1[3])
                obj5.setText(cus_ques1[4])
            cus_ques1[0] = obj1.text()
            cus_ques1[1] = obj2.text()
            cus_ques1[2] = obj3.text()
            cus_ques1[3] = obj4.text()
            cus_ques1[4] = obj5.text()
        elif item.text() == cus_ques2[0]:
            if True:
                obj1.setText(cus_ques2[0])
                obj2.setText(cus_ques2[1])
                obj3.setText(cus_ques2[2])
                obj4.setText(cus_ques2[3])
                obj5.setText(cus_ques2[4])
            cus_ques2[0] = obj1.text()
            cus_ques2[1] = obj2.text()
            cus_ques2[2] = obj3.text()
            cus_ques2[3] = obj4.text()
            cus_ques2[4] = obj5.text()
        elif item.text() == cus_ques3[0]:
            if True:
                obj1.setText(cus_ques3[0])
                obj2.setText(cus_ques3[1])
                obj3.setText(cus_ques3[2])
                obj4.setText(cus_ques3[3])
                obj5.setText(cus_ques3[4])
            cus_ques3[0] = obj1.text()
            cus_ques3[1] = obj2.text()
            cus_ques3[2] = obj3.text()
            cus_ques3[3] = obj4.text()
            cus_ques3[4] = obj5.text()
        elif item.text() == ques4[0]:
            if True:
                obj1.setText(cus_ques4[0])
                obj2.setText(cus_ques4[1])
                obj3.setText(cus_ques4[2])
                obj4.setText(cus_ques4[3])
                obj5.setText(cus_ques4[4])
            cus_ques4[0] = obj1.text()
            cus_ques4[1] = obj2.text()
            cus_ques4[2] = obj3.text()
            cus_ques4[3] = obj4.text()
            cus_ques4[4] = obj5.text()
            
def ins_clicked(self):
    ins_win.show()
save_question = QPushButton('Сохранить')
back = QPushButton('Вернутся')
v_line = QVBoxLayout()
h_line = QHBoxLayout()

ques1 = ['Перевод слова - Яблоко', 'Apply', 'Ant', 'Appart', 'Apple']
ques2 = ['Перевод слова - Piggy bank', 'Банк со свинкой', 'Банк свиньи', 'Свинья копилка', 'Свиной банк']
ques3 = ['Не являетя правильным переводом - Iron', 'Мягкий', 'Утюг', 'Железный', 'Железо']
ques4 = ['Слова, которые не были в вопросах', 'Apple', 'Свинья копилка', 'Iron', 'Твёрдость']

cus_ques1 = ['Вопрос', 'правильно', 'неправильно', 'неправильно', 'неправильно']
cus_ques2 = ['Вопрос', 'правильно', 'неправильно', 'неправильно', 'неправильно']
cus_ques3 = ['Вопрос', 'правильно', 'неправильно', 'неправильно', 'неправильно']
cus_ques4 = ['Вопрос', 'правильно', 'неправильно', 'неправильно', 'неправильно']

cus_ques = [cus_ques1[0], cus_ques2[0], cus_ques3[0], cus_ques4[0]]

ques = [ques1[0], ques2[0], ques3[0], ques4[0]]
line = QFormLayout()
obj1 = QLineEdit()
obj2 = QLineEdit()
obj3 = QLineEdit()
obj4 = QLineEdit()
obj5 = QLineEdit()

line.addRow('Вопрос' ,obj1)
line.addRow('Правильный ответ' ,obj2)
line.addRow('Неправильный ответ 1' ,obj3)
line.addRow('Неправильный ответ 2' ,obj4)
line.addRow('Неправильный ответ 3' ,obj5)

instrustion = QPushButton('Инструкция этого окна')

view = Example()
h_line.addWidget(view)
h_line.addLayout(line)
v_line.addWidget(back)
v_line.addWidget(instrustion)
layout = QVBoxLayout()
layout.addLayout(h_line)
layout.addLayout(v_line)
instrustion.clicked.connect(ins_clicked)
win_custom.setLayout(layout)


ins_win = QWidget()
ins_win.resize(400, 400)
ins_win.move(300, 300)
ins_text = QLabel('Вы можете тут игратся и веселится, но ничего не изменится в вопросах. Бета релиз сейчас.')
ins_line = QHBoxLayout()
ins_line.addWidget(ins_text)
ins_win.setLayout(ins_line)
ins_win.hide()

def clicked_save_ques(self):
    test = 0
from PyQt5.QtWidgets import *
win_custom = QWidget()
win_custom.resize(900, 400)
win_custom.move(300, 300)
win_custom.setWindowTitle('Редактор вопросов')
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.l = QListWidget()
        self.l.addItems(ques)

        self.l.itemClicked.connect(self.selectionChanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.l)
        self.setLayout(vbox)

    def selectionChanged(self, item):
        if item.text() == ques1[0]:
            if True:
                obj1.setText(ques1[0])
                obj2.setText(ques1[1])
                obj3.setText(ques1[2])
                obj4.setText(ques1[3])
                obj5.setText(ques1[4])
            ques1[0] = obj1.text()
            ques1[1] = obj2.text()
            ques1[2] = obj3.text()
            ques1[3] = obj4.text()
            ques1[4] = obj5.text()
        elif item.text() == ques2[0]:
            if True:
                obj1.setText(ques2[0])
                obj2.setText(ques2[1])
                obj3.setText(ques2[2])
                obj4.setText(ques2[3])
                obj5.setText(ques2[4])
            ques2[0] = obj1.text()
            ques2[1] = obj2.text()
            ques2[2] = obj3.text()
            ques2[3] = obj4.text()
            ques2[4] = obj5.text()
        elif item.text() == ques3[0]:
            if True:
                obj1.setText(ques3[0])
                obj2.setText(ques3[1])
                obj3.setText(ques3[2])
                obj4.setText(ques3[3])
                obj5.setText(ques3[4])
            ques3[0] = obj1.text()
            ques3[1] = obj2.text()
            ques3[2] = obj3.text()
            ques3[3] = obj4.text()
            ques3[4] = obj5.text()
        elif item.text() == ques4[0]:
            if True:
                obj1.setText(ques4[0])
                obj2.setText(ques4[1])
                obj3.setText(ques4[2])
                obj4.setText(ques4[3])
                obj5.setText(ques4[4])
            ques4[0] = obj1.text()
            ques4[1] = obj2.text()
            ques4[2] = obj3.text()
            ques4[3] = obj4.text()
            ques4[4] = obj5.text()
        ques = [ques1[0], ques2[0], ques3[0], ques4[0]]
back = QPushButton('Вернутся')
v_line = QVBoxLayout()
h_line = QHBoxLayout()
ques1 = ['Перевод слова - Яблоко', 'Apply', 'Ant', 'Appart', 'Apple']
ques2 = ['Перевод слова - Piggy bank', 'Банк со свинкой', 'Банк свиньи', 'Свинья копилка', 'Свиной банк']
ques3 = ['Не являетя правильным переводом - Iron', 'Мягкий', 'Утюг', 'Железный', 'Железо']
ques4 = ['Слова, которые не были в вопросах', 'Apple', 'Свинья копилка', 'Iron', 'Твёрдость']
ques = [ques1[0], ques2[0], ques3[0], ques4[0]]
line = QFormLayout()
obj1 = QLineEdit(ques1[0])
obj2 = QLineEdit(ques1[4])
obj3 = QLineEdit(ques1[2])
obj4 = QLineEdit(ques1[3])
obj5 = QLineEdit(ques1[1])
line.addRow('Вопрос' ,obj1)
line.addRow('Вариант ответа 1' ,obj2)
line.addRow('Вариант ответа 2' ,obj3)
line.addRow('Вариант ответа 3' ,obj4)
line.addRow('Вариант ответа 4' ,obj5)
view = Example()
h_line.addWidget(view)
h_line.addLayout(line)
v_line.addWidget(back)
layout = QVBoxLayout()
layout.addLayout(h_line)
layout.addLayout(v_line)
win_custom.setLayout(layout) 
from PyQt5.QtWidgets import *
win_custom = QWidget()
win_custom.resize(700, 400)
win_custom.move(300, 300)
win_custom.setWindowTitle('Редактор вопросов')
back = QPushButton('Вернутся')
test_line = QHBoxLayout()
test_line.addWidget(back)
win_custom.setLayout(test_line)
ques1 = ['Перевод слова - Яблоко', 'Apply', 'Ant', 'Appart', 'Apple']
ques2 = ['Перевод слова - Piggy bank', 'Банк со свинкой', 'Банк свиньи', 'Свинья копилка', 'Свиной банк']
ques3 = ['Не являетя правильным переводом - Iron', 'Мягкий', 'Утюг', 'Железный', 'Железо']
ques4 = ['Слова, которые не были в вопросах', 'Apple', 'Свинья копилка', 'Iron', 'Твёрдость']
line = QFormLayout()
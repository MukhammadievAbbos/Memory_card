from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup

from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('В каком году родился Аль - Хорезми?', '783', '985', '1885', '1007'))
questions_list.append(Question('Какая самая быстрая машина в мире?', 'Bugatti Chiron', 'Bugatti Veyron', 'Bugatti Divo', 'Pagani'))
questions_list.append(Question('Сколько истребителей в Узбекистане?', '450', '115', '250', '10'))
questions_list.append(Question('Sherzod geymi?', 'ANNIQ', 'HA', 'BALKIM','YOQ'))
questions_list.append(Question('Qaysi oyin yoqadi?', 'PUBG', 'FREE FIRE', 'FORNITE', 'CALL OF DUTY'))

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 200)

btn_ok = QPushButton('Ответить')
question = QLabel()

RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

row1 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(rbtn_1)
col1.addWidget(rbtn_2)
col2.addWidget(rbtn_3)
col2.addWidget(rbtn_4)

row1.addLayout(col1)
row1.addLayout(col2)

RadioGroupBox.setLayout(row1)


AnsGroupBox = QGroupBox('Резултат текста')
lb_result = QLabel()
lb_correct = QLabel()

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)



row2 = QHBoxLayout()
row2.addWidget(question, alignment=Qt.AlignHCenter)
row3 = QHBoxLayout()
row3.addStretch(1)
row3.addWidget(btn_ok, stretch=2)
row3.addStretch(1)
row4 = QHBoxLayout()
row4.addWidget(RadioGroupBox)
row4.addWidget(AnsGroupBox)
AnsGroupBox.hide()

col3 = QVBoxLayout()
col3.addLayout(row2, stretch=2)
col3.addLayout(row4, stretch=8)
col3.addLayout(row3, stretch=4)

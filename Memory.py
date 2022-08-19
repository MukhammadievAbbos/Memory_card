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
col3.addStretch(1)
col3.setSpacing(5)



def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    #asdasd
    RadioGroup.setExclusive(True)



def test():
    if btn_ok.text() == 'Ответить':
        show_result()
    else:
        show_question()


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()



def show_correct(res):
    lb_result.setText(res)
    show_result()    



def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')

    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Не правильно!')


def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)


def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()



main_win.cur_question = -1
next_question()
main_win.setLayout(col3)
btn_ok.clicked.connect(click_OK)
main_win.show()
app.exec_()

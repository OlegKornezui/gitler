from PyQt5.QtWidgets import *
from random import*

app = QApplication([])

window = QWidget()
window.resize(500, 500)

firstText = QLabel('Тицни, щоб дізнатися переможця')
secondText = QLabel('Іван Зупа')

knopka = QPushButton('r')
winLbl = QLabel('переможець')

line = QVBoxLayout()
line.addWidget(firstText)
line.addWidget(secondText)
line.addWidget(winLbl)
line.addWidget(knopka)
window.setLayout(line)
window.show()
def winner():
    a = str(random.randint(0,100))
    winLbl.setText(a)
knopka.clicked.connect(winner)
app.exec()

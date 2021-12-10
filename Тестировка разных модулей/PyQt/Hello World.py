import sys
from PyQt5.QtWidgets import *

def joke():
    w.setWindowTitle('What?')
    w.resize(600,800)
    Text.setText('')
    Text2 = QLabel(w)
    Text2.setText('New Text?!')
    Text.move(300,400)
    Text2.show()
    VertBox.addWidget(Text2)

def Message():
    Mess = QMessageBox()
    Mess.setText('Impressive MESSAGE!')
    Mess.setDetailedText("It's VERY IMMMMPRESSIVE MESSAGE!!!")
    Mess.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    Mess.exec_()
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w = QWidget()
    w.setWindowTitle('Hi!')

    Text = QLabel(w)
    Text.setText('Привет, начальник!')
    Text.move(160,50)
    Text.show()

    Lol = QPushButton(w)
    Lol.setText('Нажми на меня)')
    Lol.move(160,75)
    Lol.show()
    Lol.clicked.connect(joke)

    BUTTER = QPushButton(w)
    BUTTER.setText('Message на экране')
    BUTTER.move(160,100)
    BUTTER.show
    BUTTER.clicked.connect(Message)

    VertBox = QVBoxLayout(w)
    VertBox.addWidget(BUTTER)
    VertBox.addWidget(Lol)
    VertBox.addWidget(Text)

    w.show()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication,
                             QGridLayout)
from use_gif import use_gif
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initMain()
        

    def initMain(self):
        #Создание главного окна
        self.setWindowTitle('Анатомия')
        self.setWindowIcon(QtGui.QIcon('Pictures and Gif\AngPict.jpg'))
        self.setFixedSize(800,600)
        self.btnMainWindow()

        #Отображаем окно
        self.show()


    def btnMainWindow(self):
    #Создание кнопок начального окна
        ValueStart = 1
        #Задаём шрифт
        font = QtGui.QFont()
        font.setFamily('Calibri')
        font.setPointSize(16)
        font.setWeight(0)

        #Создание кнопки "Рекорды"
        btnRecords = QPushButton('Рекорды')
        btnRecords.setFixedSize(250,50)
        btnRecords.setFont(font)
        #Создание кнопки "Старт"
        btnStart = QPushButton('Старт')
        btnStart.setFixedSize(400,50)
        btnStart.setFont(font)
        btnStart.clicked.connect(START)

        #Создаём корректное отображение объектов
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addStretch(4)
        hbox.addWidget(btnStart)
        hbox.addStretch(2)
        hbox.addWidget(btnRecords)
        hbox.addStretch(4)

        vbox.addStretch(20)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        gridButStart = QGridLayout()
        gridButStart.setSpacing(10)
        gridButStart.addLayout(vbox,0,0)

        gif2 = use_gif()
        gridBack = QGridLayout()
        gridBack.addWidget(gif2.background,0,0)
        
        gridStart = QGridLayout()
        gridStart.addLayout(gridBack,0,0)
        gridStart.addLayout(gridButStart,0,0)

        self.setLayout(gridStart)



def START(self):
        btnRecords.hide()
        btnStart.hide()

        Myology = QPushButton("Миология")

        Craniology = QPushButton("Краниология")

        Artrology = QPushButton("Артрология")

        Osteology = QPushButton("Остелогия")
        #Зададим необходимое расположение кнопок
        grid123 = QGridLayout()
        grid123.addLayout(Myology,0,0)
        grid123.addLayout(Craniology,1,0)
        grid123.addLayout(Osteology,0,1)
        grid123.addLayout(Artrology,1,1)
        self.setLayout(grid123)


        

        
#Запуск приложения
if __name__ == '__main__':
    App = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    sys.exit(App.exec_())





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
        self.font = QtGui.QFont()
        self.font.setFamily('Calibri')
        self.font.setPointSize(16)
        self.font.setWeight(0)

        
        #Создание кнопки "Рекорды"
        self.btnRecords = QPushButton('Рекорды')
        self.btnRecords.setFixedSize(250,50)
        self.btnRecords.setFont(self.font)
        #Создание кнопки "Старт"
        self.btnStart = QPushButton('Старт')
        self.btnStart.setFixedSize(400,50)
        self.btnStart.setFont(self.font)
        self.btnStart.clicked.connect(self.Start)

        #Создаём корректное отображение объектов
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addStretch(4)
        hbox.addWidget(self.btnStart)
        hbox.addStretch(2)
        hbox.addWidget(self.btnRecords)
        hbox.addStretch(4)

        vbox.addStretch(20)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        gridButStart = QGridLayout()
        gridButStart.setSpacing(10)
        gridButStart.addLayout(vbox,0,0)

        gif = use_gif()
        gridBack = QGridLayout()
        gridBack.addWidget(gif.background,0,0)
        
        self.gridMain = QGridLayout()
        self.gridMain.addLayout(gridBack,0,0)
        self.gridMain.addLayout(gridButStart,0,0)

        self.setLayout(self.gridMain)

    def Start(self):
        self.btnRecords.hide()
        self.btnStart.hide()
        
        self.myology = QPushButton('Миология')
        self.myology.setFixedSize(200,50)
        self.myology.setFont(self.font)
        self.craniology = QPushButton('Краниология')
        self.craniology.setFixedSize(200,50)
        self.craniology.setFont(self.font)
        self.artrology = QPushButton('Артрология')
        self.artrology.setFixedSize(200,50)
        self.artrology.setFont(self.font)
        self.osteology = QPushButton('Остелогия')
        self.osteology.setFixedSize(200,50)
        self.osteology.setFont(self.font)
        self.myology.clicked.connect(self.btnMyology)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox1.addStretch(10)
        hbox1.addWidget(self.myology)
        hbox1.addWidget(self.artrology)
        hbox1.addStretch(10)
        hbox2.addStretch(10)
        hbox2.addWidget(self.craniology)
        hbox2.addWidget(self.osteology)
        hbox2.addStretch(10)
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        self.gridMain.addLayout(vbox,0,0)

        self.setLayout(self.gridMain)

    def btnMyology(self):
        self.myology.hide()
        self.artrology.hide()
        self.craniology.hide()
        self.osteology.hide()
        
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        vbox = QVBoxLayout()
        grid = QGridLayout()
        self.ListMyology = ['Spina', 'Спина и шея', 'Upper', 'Верхние конечности',
         'Taz', 'Мышцы таза', 'Stupni', 'Ступни',
         'Jivot', 'Грудь и живот', 'Kist', 'Кисть', 'Lower', 'Нижние конечости']
        for j in range(7):
            self.ListMyology[2*j+1] = QPushButton(self.ListMyology[2*j])
            self.ListMyology[2*j+1].setFixedSize(200,50)
            self.ListMyology[2*j+1].setFont(self.font)

        j = 0
        for k in range(3):
            if j == 0:
                hbox1.addWidget(self.ListMyology[j])
                hbox1.addWidget(self.ListMyology[j+2])
                hbox1.addWidget(self.ListMyology[j+4])
                j = j + 6
            elif j == 6:
                hbox2.addWidget(self.ListMyology[j])
                hbox2.addWidget(self.ListMyology[j+2])
                hbox2.addWidget(self.ListMyology[j+4])
                j == -2
            else:
                hbox3.addWidget(self.ListMyology[j])

        vbox.addStretch(5)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(5)

        self.gridMain.addLayout(vbox,0,0)
        self.setLayout(self.gridMain)
                
                
                
            
        
            
                        
            
        
        




        

        
#Запуск приложения
if __name__ == '__main__':
    App = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    sys.exit(App.exec_())





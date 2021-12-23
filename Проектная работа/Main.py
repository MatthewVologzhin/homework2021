from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication,
                             QGridLayout, QLabel, QLineEdit)
from PyQt5.QtGui import (QPixmap)
from use_gif import use_gif
import sys
import sip
import random as r
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ListMyology = ['self.btnSpina', 'Спина и шея', 'self.btnUpper', 'Верхние конечности',
         'self.btnTaz', 'Мышцы таза', 'self.btnStupni', 'Ступни',
         'self.btnJivot', 'Грудь и живот', 'self.btnKist', 'Кисть', 'self.btnLower', 'Нижние конечости']
        self.initMain()


    def initMain(self):
        #Создание главного окна
        self.setWindowTitle('Анатомия')
        self.setWindowIcon(QtGui.QIcon('Pictures and Gif\AngPict.jpg'))
        self.setFixedSize(1920,1000)
        self.btnMainWindow()


    def btnMainWindow(self, howManyClick = 3):
    #Создание кнопок начального окна
        self.i = 0
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
        #Создание кнопки "Сменить тему"
        #self.btnChangeTheme = QPushButton("Изменить тему")
        #self.btnChangeTheme.setFixedSize(200,50)
        #self.btnChangeTheme.setFont(self.font)
        #self.btnChangeTheme.clicked.connect(self.ChangeTheme)

        #Создание заставки
        self.mainPict = QLabel()
        pict = QPixmap('Pictures and Gif/anatomy.png')
        self.mainPict.setPixmap(pict)

        #Создаём корректное отображение объектов
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hboxChange = QHBoxLayout()
        vboxChange = QVBoxLayout()
        gridButStart = QGridLayout()
        self.gridMain = QGridLayout()
        vboxMAIN = QVBoxLayout()
        hboxMAIN = QHBoxLayout()
        gridBack = QGridLayout()

        hbox.addStretch(4)
        hbox.addWidget(self.btnStart)
        hbox.addStretch(2)
        hbox.addWidget(self.btnRecords)
        hbox.addStretch(4)
        vbox.addStretch(20)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        vboxMAIN.addStretch(1)
        vboxMAIN.addWidget(self.mainPict)
        vboxMAIN.addStretch(1)
        hboxMAIN.addStretch(1)
        hboxMAIN.addLayout(vboxMAIN)
        hboxMAIN.addStretch(1)

        #vboxChange.addWidget(self.btnChangeTheme)
        #vboxChange.addStretch(1)
        #hboxChange.addStretch(1)
        #hboxChange.addLayout(vboxChange)

        gridButStart.setSpacing(10)
        gridButStart.addLayout(vbox,0,0)

        self.gif = use_gif(howManyClick)
        gridBack.addWidget(self.gif.background,0,0)
        gridBack.addLayout(hboxChange,0,0)
        gridBack.addLayout(hboxMAIN,0,0)
        
        self.gridMain.addLayout(gridBack,0,0)
        self.gridMain.addLayout(gridButStart,0,0)

        self.setLayout(self.gridMain)

    #Функционал кнопки "Старт"
    def Start(self):

        #Убираем старые кнопки, задаём новые
        self.btnRecords.hide()
        self.btnStart.hide()
        self.mainPict.hide()
        
        self.myology = QPushButton('Миология')
        self.myology.setFixedSize(200,50)
        self.myology.setFont(self.font)
        self.myology.clicked.connect(self.btnMyology)
        self.craniology = QPushButton('Краниология')
        self.craniology.setFixedSize(200,50)
        self.craniology.setFont(self.font)
        self.artrology = QPushButton('Артрология')
        self.artrology.setFixedSize(200,50)
        self.artrology.setFont(self.font)
        self.osteology = QPushButton('Остеология')
        self.osteology.setFixedSize(200,50)
        self.osteology.setFont(self.font)

        self.btnBack = QPushButton('Вернуться')
        self.btnBack.setFixedSize(140,50)
        self.btnBack.setFont(self.font)
        

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()
        vboxBack = QVBoxLayout()
        hboxBack = QHBoxLayout()

        vboxBack.addStretch(1)
        vboxBack.addWidget(self.btnBack)
        hboxBack.addStretch(1)
        hboxBack.addLayout(vboxBack)

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
        self.gridMain.addLayout(hboxBack,0,0)

        self.setLayout(self.gridMain)

    #Смена темы. В разработке.
    def ChangeTheme(self, howManyClick = 0):
            howManyClick = howManyClick + 1
            if howManyClick == 2:
                howManyClick = 0
                self.btnMainWindow(howManyClick = howManyClick)
            else:
                self.btnMainWindow(howManyClick = howManyClick)
        
        
    #Функционал кнопки "Миология"
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
        for j in range(7):
            self.ListMyology[2*j] = QPushButton(self.ListMyology[2*j+1])
            self.ListMyology[2*j].setFixedSize(250,50)
            self.ListMyology[2*j].setFont(self.font)
            if j == 0:
                self.ListMyology[0].clicked.connect(self.Spina)

        j = 0
        for k in range(3):
            if j == 0:
                hbox1.addStretch(1)
                hbox1.addWidget(self.ListMyology[j])
                hbox1.addWidget(self.ListMyology[j+2])
                hbox1.addWidget(self.ListMyology[j+4])
                hbox1.addStretch(1)
                j = j + 6
            elif j == 6:
                hbox2.addStretch(1)
                hbox2.addWidget(self.ListMyology[j])
                hbox2.addWidget(self.ListMyology[j+2])
                hbox2.addWidget(self.ListMyology[j+4])
                hbox2.addStretch(1)
                j = 12
            else:
                hbox3.addStretch(1)
                hbox3.addWidget(self.ListMyology[j])
                hbox3.addStretch(1)

        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)

        self.gridMain.addLayout(vbox,0,0)
        self.setLayout(self.gridMain)


#Класс объектов теста
    class QuestionWidget(QWidget):
        def __init__(self):
            super().__init__()
            self.Main()

        def Main(self):

            self.font = QtGui.QFont()
            self.font.setFamily('Calibri')
            self.font.setPointSize(16)
            self.font.setWeight(0)

            numb = r.randint(1,2)
            direct = 'spina'
            self.testPict = QLabel()
            pict = QPixmap('Pictures and Gif/test_pictures/%s/%d.png' % (direct,numb))
            self.testPict.setPixmap(pict)

            btnNext = QPushButton('Принять')
            btnSkip = QPushButton('Пропустить')
            btnNext.setFixedSize(140,40)
            btnSkip.setFixedSize(140,40)
            btnNext.setFont(self.font)
            btnSkip.setFont(self.font)
            AnsLine = QLineEdit()
            AnsLine.setFixedSize(250,40)


            hboxPict = QHBoxLayout()
            hboxBtn = QHBoxLayout()
            hboxLine = QHBoxLayout()
            vboxF = QVBoxLayout()
            self.gridTest = QGridLayout()
            hboxPict.addStretch(1)
            hboxPict.addWidget(self.testPict)
            hboxPict.addStretch(1)
            hboxLine.addStretch(1)
            hboxLine.addWidget(AnsLine)
            hboxLine.addStretch(1)
            hboxBtn.addStretch(30)
            hboxBtn.addWidget(btnNext)
            hboxBtn.addStretch(1)
            hboxBtn.addWidget(btnSkip)
            hboxBtn.addStretch(30)
            vboxF.addStretch(10)
            vboxF.addLayout(hboxPict)
            vboxF.addStretch(1)
            vboxF.addLayout(hboxLine)
            vboxF.addStretch(1)
            vboxF.addLayout(hboxBtn)
            vboxF.addStretch(10)
            self.gridTest.addLayout(vboxF,0,0)


            
            
            
            

        

    #Функционал кнопки "Спина"
    def Spina(self):
        self.btnBack.hide()
        for i in range(7):
            self.ListMyology[2*i].hide()
        SpinaTest = self.QuestionWidget()
        self.gridMain.addLayout(SpinaTest.gridTest,0,0)


        


#Запуск приложения
if __name__ == '__main__':
    App = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    #Отображаем окно
    mainWindow.show()
    sys.exit(App.exec_())

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QPixmap)
from use_gif import use_gif
import sys
import sip
import random as r
import datetime as t
import os
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.hmcl = 2
        self.ListMyology = ['self.btnSpina', 'Спина и шея', 'self.btnUpper', 'Верхние конечности',
         'self.btnTaz', 'Мышцы таза', 'self.btnStupni', 'Ступни',
         'self.btnJivot', 'Грудь и живот', 'self.btnKist', 'Кисть', 'self.btnLower', 'Нижние конечости']
        self.initMain()



    def initMain(self):
        #Создание главного окна
        self.setWindowTitle('Анатомия')
        self.setWindowIcon(QtGui.QIcon('Pictures and Gifs\AngPict.png'))
        self.setFixedSize(1920,1000)
        self.btnMainWindow()

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = (ag.width() - widget.width())/2
        y = (2 * ag.height() - sg.height() - widget.height())/2
        self.move(x, y)


    def btnMainWindow(self, howManyClick = 2):
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
        self.btnChangeTheme = QPushButton("Изменить тему")
        self.btnChangeTheme.setFixedSize(200,50)
        self.btnChangeTheme.setFont(self.font)
        self.btnChangeTheme.clicked.connect(self.ChangeTheme)

        #Создание заставки
        self.mainPict = QLabel()
        pict = QPixmap('Pictures and Gifs/anatomy.png')
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
        mainWidget = QWidget()

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

        vboxChange.addWidget(self.btnChangeTheme)
        vboxChange.addStretch(1)
        hboxChange.addStretch(1)
        hboxChange.addLayout(vboxChange)

        gridButStart.setSpacing(10)
        gridButStart.addLayout(vbox,0,0)
        self.gif = use_gif(howManyClick = self.hmcl)
        gridBack.addWidget(self.gif.background,0,0)
        gridBack.addLayout(hboxChange,0,0)
        gridBack.addLayout(hboxMAIN,0,0)
        
        self.gridMain.addLayout(gridBack,0,0)
        self.gridMain.addLayout(gridButStart,0,0)
        mainWidget.setLayout(self.gridMain)
        self.setCentralWidget(mainWidget)


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
        self.btnBack.clicked.connect(self.btnMainWindow)
        

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


    #Смена темы. В разработке.
    def ChangeTheme(self):
        if self.hmcl != 10:
            self.hmcl = self.hmcl + 1
            self.btnMainWindow(self.hmcl)
        else:
            self.hmcl = 1
            self.btnMainWindow(self.hmcl)
        
        
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

    
    #Функционал кнопки "Спина"
    def Spina(self):
        self.spinaWidget = QWidget()
        self.btnBack.hide()
        self.btnChangeTheme.hide()
        self.HMQ = HMQuestions()
        self.HMQ.location_on_the_screen()
        self.HMQ.show()
        self.HMQ.btnAccept.clicked.connect(self.Accept)

        for i in range(7):
            self.ListMyology[2*i].hide()
            
        self.SpinaTest = QuestionWidget('spina')
        self.counter = 1
        self.gridMain.addWidget(self.SpinaTest,0,0)
        self.spinaWidget.setLayout(self.gridMain)
        self.setCentralWidget(self.spinaWidget)

        self.SpinaTest.btnNext.clicked.connect(self.Next)

        self.trueCounter = 0

    def Next(self):
        if self.SpinaTest.AnsLine.currentText() == self.SpinaTest.analyseList[self.SpinaTest.QuestionNumber]:
            self.trueCounter = self.trueCounter + 1    

        if self.counter >= int(self.NumbQuest):
            self.w = FinalWindow(self.trueCounter, self.NumbQuest)
            self.w.show()
            self.SpinaTest.setParent(None)
            self.btnMainWindow()
            
        else:
            newWidget = QuestionWidget('spina')
            self.gridMain.replaceWidget(self.SpinaTest, newWidget)
            self.SpinaTest.setParent(None)
            self.SpinaTest = newWidget
            self.SpinaTest.btnNext.clicked.connect(self.Next)
            self.counter = self.counter + 1
            self.SpinaTest.Accepted()
            print(self.counter)

    def Accept(self):
        self.NumbQuest = self.HMQ.line.text()
        if self.NumbQuest.isdigit() == True:
            print(self.HMQ.line.text())
            self.HMQ.hide()
            self.SpinaTest.Accepted()


#Окно с результатом
class FinalWindow(QMainWindow):
    def __init__(self, trueCounter, NumbQuest):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('Pictures and Gifs\AngPict.png'))
        self.setFixedSize(400,200)
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = (ag.width() - widget.width())/2
        y = (2*ag.height() - sg.height() - widget.height())/2
        self.move(x,y)

        self.setWindowTitle('Результат')
        result = QLabel()
        hbox = QHBoxLayout()
        widget = QWidget()
        
        result.setText('Ваш результат: %s' % (trueCounter) + ' правильный ответ из ' + str(NumbQuest) +
                       '\n' + str((int(trueCounter)/int(NumbQuest))) + '%')
        hbox.addStretch(1)
        hbox.addWidget(result)
        hbox.addStretch(1)
        widget.setLayout(hbox)
        
        self.setCentralWidget(widget)




        
        
        
            

#Класс объектов теста
class QuestionWidget(QWidget):
    def __init__(self,direct,parent = None):
            super().__init__(parent=parent)
            self.direct = direct

            self.btnNext = QPushButton('Принять')
            self.btnNext.setFixedSize(200,40)

    def Accepted(self):
            self.font = QtGui.QFont()
            self.font.setFamily('Calibri')
            self.font.setPointSize(16)
            self.font.setWeight(0)
            fontAns = QtGui.QFont()
            fontAns.setFamily('Calibri')
            fontAns.setPointSize(13)
            fontAns.setWeight(0)
            
            self.numb = r.randint(1,14)
            self.testPict = QLabel()
            pict = QPixmap('Pictures and Gifs/test_pictures/%s/%d.png' % (self.direct,self.numb))
            self.testPict.setPixmap(pict)

            self.AnsLine = QComboBox()
            self.AnsLine.setFont(fontAns)
            self.AnsLine.setFixedSize(400,40)

            with open('Questions and Answers/%s/%d.txt' % (self.direct,self.numb)) as testText:
                QuestionNumber = ''
                HWLines = 0
                NumbOfQuestions = []
                ListOfAnswers = []
                self.analyseList = {}
                for lines in testText:
                    HWLines = HWLines + 1
                    lines1 = lines.split(')')
                    if lines1[1].find('\n') != -1:
                        lines1[1] = lines1[1].replace('\n', '')
                    NumbOfQuestions.append(lines1[0])
                    ListOfAnswers.append(lines1[1])
                    self.analyseList[lines1[0]] = lines1[1]
                print(self.analyseList)
                NumbOfQuestions1 = NumbOfQuestions
                r.shuffle(NumbOfQuestions1)
                for i in NumbOfQuestions1:
                    self.AnsLine.addItems([self.analyseList[i]])

                self.QuestionNumber = NumbOfQuestions[r.randint(0,HWLines-1)]

            self.testWidget = QWidget()
            Question = QLabel()
            Question.setText('Введите название %s:' % (self.QuestionNumber))
            Question.setFont(self.font)
            Question.setStyleSheet('QLabel {color: white}')
            self.btnNext.setFont(self.font)


            grid = QGridLayout()
            hbox = QHBoxLayout()
            vbox = QVBoxLayout()
            hbox2 = QHBoxLayout()
            hbox1 = QHBoxLayout()
            hbox3 = QHBoxLayout()

            hbox.addStretch(1)
            hbox.addWidget(self.testPict)
            hbox.addStretch(1)
            hbox1.addStretch(1)
            hbox1.addWidget(Question)
            hbox1.addStretch(1)
            hbox2.addStretch(1)
            hbox2.addWidget(self.AnsLine)
            hbox2.addStretch(1)
            hbox3.addStretch(1)
            hbox3.addWidget(self.btnNext)
            hbox3.addStretch(1)
            vbox.addStretch(1)
            vbox.addLayout(hbox)
            vbox.addLayout(hbox1)
            vbox.addLayout(hbox2)
            vbox.addLayout(hbox3)
            vbox.addStretch(1)
            self.setLayout(vbox)
        

    def __del__(self):
            print('Deleted')

class HMQuestions(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('Pictures and Gifs\AngPict.png'))
        self.font = QtGui.QFont()
        self.font.setFamily('Calibri')
        self.font.setPointSize(13)
        self.font.setWeight(0)
        self.setFixedSize(300,140)
        self.setWindowTitle(' ')

        self.line = QLineEdit()
        self.line.setFixedSize(200,34)
        self.line.setAlignment(QtCore.Qt.AlignCenter)
        self.line.setFont(self.font)
        text = QLabel()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        vbox = QVBoxLayout()
        self.btnAccept = QPushButton()
        self.btnAccept.setText('Принять')
        self.btnAccept.setFont(self.font)
        self.btnAccept.setFixedSize(150,44)
        
        text.setText('Кол-во вопросов в тесте:')
        text.setFont(self.font)

        hbox1.addStretch(1)
        hbox1.addWidget(text)
        hbox1.addStretch(1)
        hbox2.addStretch(1)
        hbox2.addWidget(self.line)
        hbox2.addStretch(1)
        hbox3.addStretch(1)
        hbox3.addWidget(self.btnAccept)
        hbox3.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        vbox.addStretch(1)
        
        widget = QWidget()
        grid = QGridLayout()

        grid.addLayout(vbox,0,0)
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = (ag.width() - widget.width())/2
        y = (2 * ag.height() - sg.height() - widget.height())/2
        self.move(x, y)
    
        
        

#Запуск приложения
if __name__ == '__main__':
    App = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.location_on_the_screen()
    #Отображаем окно
    mainWindow.show()
    sys.exit(App.exec_())

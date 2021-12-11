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
        
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        vbox = QVBoxLayout()
        grid = QGridLayout()
        gridMain = QGridLayout()
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

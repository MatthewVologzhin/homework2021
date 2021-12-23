from PyQt5 import QtGui, QtWidgets, QtCore
import sys

class use_gif():
    def __init__(self, howManyClick):
        self.background = QtWidgets.QLabel()
        self.background.setGeometry(QtCore.QRect(0,0,800,600))
        List = ['gif_black', 'gif_white', 'LoL','1']
        self.movie = QtGui.QMovie(f'Pictures and Gif\{List[howManyClick]}.gif')
        
        self.background.setMovie(self.movie)
        self.movie.start()


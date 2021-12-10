from PyQt5 import QtGui, QtWidgets, QtCore
import sys

class use_gif():
    def __init__(self):
        self.background = QtWidgets.QLabel()
        self.background.setGeometry(QtCore.QRect(0,0,800,600))
        self.movie = QtGui.QMovie('Pictures and Gif\gif_black.gif')
        
        self.background.setMovie(self.movie)
        self.movie.start()


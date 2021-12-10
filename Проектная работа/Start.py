def START(self):
        btnRecords.hide()
        btnStart.hide()

        Myology = QPushButton("Миология")
        Myology.setFixedSize(200,50)

        Craniology = QPushButton("Краниология")
        Craniology.setFixedSize(200,50)

        Artrology = QPushButton("Артрология")
        Artrology.setFixedSize(200,50)

        Osteology = QPushButton("Остелогия")
        Osteology.setFixedSize(200,50)

        BackToStart = QPushButton("Вернуться в начало")
        BackToStart.setFixedSize(100,25)

        #Зададим необходимое расположение кнопок
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayput()
        vbox1 = QVBoxLayout()

        hbox1.addStretch(4)
        hbox1.addWidget(Myology)
        hbox1.addStretch(2)
        hbox1.addWidget(Craniology)
        hbox1.addStretch(4)
        hbox2.addStretch(4)
        hbox2.addWidget(Artrology)
        hbox2.addStretch(2)
        hbox2.addWidget(Osteology)
        hbox2.addStretch(4)
        vbox1.addStretch(4)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addStretch(4)

        self.setLayout(vbox1)

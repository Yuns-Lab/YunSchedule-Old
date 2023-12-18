# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QFrame, QWidget

from views.Controls.homeControls import ClockWidget, TimeWidget, DateWidget

class HomeInterface(QFrame):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent = parent)
        self.setObjectName('homeInterfaceWidget')
        self.__initWidget()
    #
    def __initWidget(self):
        self.timeTitleFrame = QFrame()
        self.setObjectName('timeTitleFrame')
        #
        clock = ClockWidget(self)
        clock.resize(300, 300)
        clock.move(40, 40)
        #
        time = TimeWidget(self)
        time.move(455, 110)
        #
        date = DateWidget(self)
        date.move(435, 220)
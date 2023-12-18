# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QFrame, QWidget

class homeInterface(QFrame):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent = parent)
        self.setObjectName('homeInterfaceWidget')
        self.__initTitleWidget()
    #
    def __initTitleWidget(self):
        self.timeTitleFrame = QFrame()
        self.setObjectName('timeTitleFrame')
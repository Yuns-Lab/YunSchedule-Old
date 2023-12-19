# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QFrame, QWidget, QGridLayout

from widgets.homeControls import ClockWidget, TimeDateWidget, PlanWidget

class HomeInterface(QFrame):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent = parent)
        self.setObjectName('homeInterfaceWidget')
        self.__initWidget()
        self.__initLayout()
    #
    def __initWidget(self):
        self.timeTitleFrame = QFrame()
        self.setObjectName('timeTitleFrame')
        #
        self.clock = ClockWidget(self)
        self.clock.resize(300, 300)
        #
        self.TimeDateWidget = TimeDateWidget(self)
        #
        self.plan = PlanWidget(self)
    #
    def __initLayout(self):
        layout = QGridLayout(self)
        self.setLayout(layout)
        #
        layout.setColumnStretch(0, 7)
        layout.setColumnMinimumWidth(1, 300)
        layout.setColumnStretch(2, 10)
        layout.setColumnStretch(3, 10)
        layout.setColumnStretch(4, 7)
        
        layout.setRowStretch(0, 2)
        layout.setRowMinimumHeight(1, 300)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 10)
        layout.setRowStretch(4, 2)
        #
        layout.addWidget(self.clock, 1, 1)
        layout.addWidget(self.TimeDateWidget, 1, 3)
        layout.addWidget(self.plan, 3, 1, 3, 1)
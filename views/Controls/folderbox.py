# -*- coding:utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFrame
from PyQt5.QtGui import QIcon

from qfluentwidgets import FluentIcon as FIF

class TodayPlanBox(QWidget):
    def __init__(self, parent: QFrame, width: int, height: int, boxTitle: str):
        super().__init__()
        self.setFixedSize(width, height)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        folderBox = QWidget(self)
        folderBox.setObjectName("folderBox")
        layout.addWidget(folderBox)

        boxLayout = QVBoxLayout(folderBox)
        boxLayout.setContentsMargins(0, 0, 0, 0)

        folderHead = QWidget(folderBox)
        folderHead.setObjectName("folderHead")
        folderHead.setFixedSize(387, 70)
        titleLabel = QLabel(boxTitle, folderHead)
        titleLabel.setObjectName("titleText")
        titleIcon = QLabel()
        titleIcon.setPixmap(QIcon(FIF.path(FIF.CALENDAR)).pixmap(16, 16))
        titleIcon.setObjectName("titleIcon")
        headLayout = QHBoxLayout(folderHead)
        headLayout.addWidget(titleLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        boxLayout.addWidget(folderHead)

        folderContent = QWidget(folderBox)
        folderContent.setObjectName("folderContent")
        contentLayout = QVBoxLayout(folderContent)
        contentLayout.setContentsMargins(12, 12, 12, 12)
        boxLayout.addWidget(folderContent)

        parent.addWidget(self)

    def move(self, x, y):
        self.move(x, y)

    def addWidget(self, widget: QWidget):
        self.addWidget(widget=widget, stretch=0, alignment=Qt.AlignTop)

    def createASignalElement():
        pass
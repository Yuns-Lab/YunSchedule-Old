# -*- coding:utf-8 -*-

from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QWidget

from qfluentwidgets import FluentIcon as FIF

from common.icons import Icon as LYI
from views.controls.folderbox import TodayPlanBox

class HomeInterface(QFrame):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent = parent)
        self.setObjectName('homeInterfaceWidget')
        vBoxLayout = self.__init_timeTitle(self)
        self.__init_folderBox(vBoxLayout)
    #
    def __init_timeTitle(self, parent):
        self.timeTitleFrame = QFrame(parent)
        self.setObjectName('timeTitleFrame')
        #
        timeTitleLayout = QHBoxLayout()
        timeTitleLayout.setSpacing(30)
        #
        iconDate = QIcon(FIF.path(FIF.DATE_TIME))
        pixmapIcondDate = iconDate.pixmap(48, 48)
        now = datetime.now()
        dayStr = [
            self.tr('Monday'),
            self.tr('Tuesday'),
            self.tr('Wednesday'),
            self.tr('Thursday'),
            self.tr('Friday'),
            self.tr('Saturday'),
            self.tr('Sunday')
            ][now.weekday()]
        dateStr = self.tr('Now is {}-{}-{} {}:{}:{}')
        dateStr = dateStr.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        formatted_time = f'{dateStr}，{dayStr}'
        iconTime = QIcon(FIF.path(FIF.BRIGHTNESS) if 5 < int(now.strftime('%H')) < 17 else LYI.path(LYI.MOON))
        pixmapIconTime = iconTime.pixmap(48, 48)
        #
        self.iconDateLabel = QLabel()
        self.iconDateLabel.setPixmap(pixmapIcondDate)
        #
        self.timeLabel = QLabel(formatted_time)
        self.timeLabel.setObjectName('timeLabel')
        #
        self.iconTimeLabel = QLabel()
        self.iconTimeLabel.setPixmap(pixmapIconTime)
        #
        timeTitleLayout.addWidget(self.iconDateLabel, 0)
        timeTitleLayout.addWidget(self.timeLabel, 1)
        timeTitleLayout.addWidget(self.iconTimeLabel, 2)
        #
        self.timeTitleFrame.setLayout(timeTitleLayout)
        #
        vBoxLayout = QVBoxLayout(self)
        #
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        vBoxLayout.addItem(spacerItem)
        #
        vBoxLayout.addWidget(self.timeTitleFrame, 0, Qt.AlignCenter)
        vBoxLayout.addStretch(1)
        # leave some space for title bar
        vBoxLayout.setContentsMargins(30, 32, 30, 0)
        # return vBoxLayout for init folderBox
        return vBoxLayout
    #
    def __init_folderBox(self, parent):
        folderBox = TodayPlanBox(parent=parent, width=407, height=596, boxTitle='今日计划')
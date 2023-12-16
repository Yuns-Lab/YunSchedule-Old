# -*- coding:utf-8 -*-

from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QWidget, QGridLayout

from qfluentwidgets import FluentIcon as FIF

from common.icons import Icon as LYI
from common.thread import TimeTitleUpdateThread as TTUT

class homeInterface(QFrame):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent = parent)
        self.setObjectName('homeInterfaceWidget')
        self.__initTitleWidget()
        self.__init_layout()
    #
    def __initTitleWidget(self):
        self.timeTitleFrame = QFrame()
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
        timeReplaceDict = {0:'00', 1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09'}
        hour = timeReplaceDict[now.hour] if now.hour < 10 else now.hour
        minute = timeReplaceDict[now.minute] if now.minute < 10 else now.minute
        second = timeReplaceDict[now.second] if now.second < 10 else now.second
        dateStr = dateStr.format(now.year, now.month, now.day, hour, minute, second)
        formatted_time = f'{dateStr}，{dayStr}'
        iconTime = QIcon(FIF.path(FIF.BRIGHTNESS) if 5 < int(now.strftime('%H')) < 17 else LYI.path(LYI.MOON))
        pixmapIconTime = iconTime.pixmap(48, 48)
        #
        self.iconDateLabel = QLabel()
        self.iconDateLabel.setPixmap(pixmapIcondDate)
        #
        self.timeLabel = QLabel(formatted_time)
        self.timeLabel.setObjectName('timeLabel')
        self.timeLabelUpdateThread = TTUT()
        self.timeLabelUpdateThread.signal.connect(self.on_thread_ttut_message)
        self.timeLabelUpdateThread.start()
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
    def on_thread_ttut_message(self, message):
        ''' For Thread "timeLabelUpdateThread" '''
        self.timeLabel.setText(message)
    #
    def __init_layout(self):
        vBoxLayout = QVBoxLayout(self)
        #
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        vBoxLayout.addItem(spacerItem)
        #
        vBoxLayout.addWidget(self.timeTitleFrame, 0, Qt.AlignCenter)
        vBoxLayout.addStretch(1)
        # leave some space for title bar
        vBoxLayout.setContentsMargins(30, 32, 30, 0)
        # add to page
        self.setLayout(vBoxLayout)
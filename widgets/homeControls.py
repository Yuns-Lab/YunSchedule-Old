# -*- coding:utf-8 -*-
from math import cos, sin, radians
from datetime import datetime

from PyQt5.QtCore import Qt, QTimer, QDateTime, QPointF
from PyQt5.QtGui import QColor, QPainter, QPaintEvent, QPen, QLinearGradient, QBrush, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout

from qfluentwidgets import isDarkTheme
from qfluentwidgets import FluentIcon as FIF

from common.color import hex2rgb
from common.icons import Icon as LYI

class ClockWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_hour = 0
        self.current_minute = 0
        self.current_second = 0
        # Init Update
        self.update_time()
        # Update per 1000ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    #
    def update_time(self):
        current_utc_time = QDateTime.currentDateTime()
        current_time = current_utc_time.toLocalTime().time()
        self.current_hour = current_time.hour()
        self.current_minute = current_time.minute()
        self.current_second = current_time.second()
        self.update()
    #
    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # Draw Outline
        gradient = QLinearGradient(event.rect().center().x(), event.rect().top(), event.rect().center().x(), event.rect().bottom())
        color0hex = hex2rgb('#34C0F0') if isDarkTheme() else hex2rgb('#037CD6')
        Qcolor0 = QColor()
        Qcolor0.setRgb(color0hex.r(), color0hex.g(), color0hex.b(), 255)
        color1hex = hex2rgb('#70EAFF') if isDarkTheme() else hex2rgb('#34C0F0')
        Qcolor1 = QColor()
        Qcolor1.setRgb(color1hex.r(), color1hex.g(), color1hex.b(), 255)
        gradient.setColorAt(0, Qcolor0)
        gradient.setColorAt(1, Qcolor1)
        outer_radius = min(self.width(), self.height()) * 0.4
        outer_center = self.rect().center()
        start_angle = 0
        span_angle = 360 * 16
        pen = QPen(gradient, 10)
        painter.setPen(pen)
        painter.drawArc(int(outer_center.x() - outer_radius),
                        int(outer_center.y() - outer_radius),
                        int(outer_radius * 2),
                        int(outer_radius * 2),
                        start_angle, span_angle)
        # Draw Hour Hand
        hour_radius = outer_radius * 0.4
        hour_angle = ((360 - self.current_hour * 30) % 360) + 90
        hour_point = outer_center + hour_radius * QPointF(cos(radians(hour_angle)), -sin(radians(hour_angle)))
        pen = QPen(Qt.white, 5) if isDarkTheme() else QPen(Qt.black, 5)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawLine(outer_center, hour_point)
        # Draw Minute Hand
        minute_radius = outer_radius * 0.6
        minute_angle = ((360 - self.current_minute * 6) % 360) + 90
        minute_point = outer_center + minute_radius * QPointF(cos(radians(minute_angle)), -sin(radians(minute_angle)))
        pen = QPen(Qt.white, 5) if isDarkTheme() else QPen(Qt.black, 5)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawLine(outer_center, minute_point)
        # Draw Second Hand
        second_radius = outer_radius * 0.8
        second_angle = ((360 - self.current_second * 6) % 360) + 90
        second_point = outer_center + second_radius * QPointF(cos(radians(second_angle)), -sin(radians(second_angle)))
        pen = QPen(Qt.red, 3)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawLine(outer_center, second_point)
        painter.rotate(0)
        # Draw Center Circle
        center_color_hex = '#525252' if isDarkTheme() else '#CCCCCC'
        center_color_rgb = hex2rgb(center_color_hex)
        center_color = QColor()
        center_color.setRgb(center_color_rgb.r(), center_color_rgb.g(), center_color_rgb.b(), 255)
        center_radius = 15.14
        center_point = self.rect().center()
        pen = QPen(Qt.NoPen)
        brush = QBrush(center_color)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(center_point, center_radius, center_radius)

class TimeWidget(QWidget):
    timeReplaceDict = {0:'00', 1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09'}
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init_contents()
    #
    def __init_contents(self):
        hBoxLayout = QHBoxLayout(self)
        hBoxLayout.setContentsMargins(0, 0, 0, 0)
        #
        now = datetime.now()
        hour = self.timeReplaceDict[now.hour] if now.hour < 10 else now.hour
        minute = self.timeReplaceDict[now.minute] if now.minute < 10 else now.minute
        second = self.timeReplaceDict[now.second] if now.second < 10 else now.second
        #
        iconTime = QIcon(FIF.path(FIF.BRIGHTNESS) if 5 < int(now.strftime('%H')) < 17 else LYI.path(LYI.MOON))
        pixmapIconTime = iconTime.pixmap(48, 48)
        iconLabel = QLabel()
        iconLabel.setPixmap(pixmapIconTime)
        #
        self.timeLabel = QLabel(f'{hour}:{minute}:{second}')
        self.timeLabel.setObjectName('timeLabel')
        #
        hBoxLayout.addWidget(iconLabel, 0, Qt.AlignCenter)
        hBoxLayout.addWidget(self.timeLabel, 1, Qt.AlignCenter)
        self.update_time()
        # Update per 1000ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    def update_time(self):
        now = datetime.now()
        hour = self.timeReplaceDict[now.hour] if now.hour < 10 else now.hour
        minute = self.timeReplaceDict[now.minute] if now.minute < 10 else now.minute
        second = self.timeReplaceDict[now.second] if now.second < 10 else now.second
        self.timeLabel.setText(f'{hour}:{minute}:{second}')

class DateWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init_contents()
    #
    def __init_contents(self):
        hBoxLayout = QHBoxLayout(self)
        hBoxLayout.setContentsMargins(0, 0, 0, 0)
        #
        now = datetime.now()
        #
        iconDate = QIcon(FIF.path(FIF.DATE_TIME))
        pixmapIconDate = iconDate.pixmap(48, 48)
        iconLabel = QLabel()
        iconLabel.setPixmap(pixmapIconDate)
        #
        self.dateLabel = QLabel(f'{now.year}.W{now.month}.{now.day} ')
        self.dateLabel.setObjectName('dateLabel')
        #
        hBoxLayout.addWidget(self.dateLabel, 0, Qt.AlignCenter)
        hBoxLayout.addWidget(iconLabel, 1, Qt.AlignCenter)
        self.update_time()
        # Update per 1000ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    def update_time(self):
        now = datetime.now()
        self.dateLabel.setText(f'{now.year}.{now.month}.{now.day} ')

class TimeDateWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.__init_contents()
    #
    def __init_contents(self):
        time = TimeWidget()
        date = DateWidget()
        layout = QVBoxLayout()
        layout.addWidget(time)
        layout.addWidget(date)
        time.setContentsMargins(20, 40, 0, 40)
        self.setLayout(layout)

class PlanWidget(QWidget):
    def __init__(self, parent = None, text = None):
        super().__init__(parent=parent)
        self.text = text
        self.__init_widget()
    #
    def __init_widget(self):
        self.titleLabel = QLabel(self.text)
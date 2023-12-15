# -*- coding:utf-8 -*-
from sys import argv

from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtWidgets import QApplication

from common.resource import grp
from views.main_window import Window

if __name__  ==  '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    #
    app = QApplication(argv)
    #
    translator = QTranslator()
    translator.load(grp('resource/i18N/zh_CN.qm'))
    app.installTranslator(translator)
    #R
    w = Window()
    w.show()
    app.exec_()
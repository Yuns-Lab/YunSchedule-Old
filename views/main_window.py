# -*- coding:utf-8 -*-
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices, QFontDatabase
from PyQt5.QtWidgets import QApplication, QStackedWidget, QHBoxLayout

from qfluentwidgets import NavigationInterface, NavigationItemPosition, MessageBox, Theme, isDarkTheme, setTheme, qrouter
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow

from widgets.windowControls import AvatarWidget, CustomTitleBar

from views.blank_interface import Widget
from views.home_interface import HomeInterface
from views.setting_interface import SettingInterface

from common.resource import grp
from common.config import Config

class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBar(CustomTitleBar(self))
        # use theme in config
        config = Config()
        q_fluent_widgets = config.getConfig("QFluentWidgets")
        theme_mode = {
            'Light': Theme.LIGHT,
            'Dark': Theme.DARK,
            'Auto': Theme.AUTO
        }[q_fluent_widgets["ThemeMode"]] if q_fluent_widgets != None else Theme.AUTO
        setTheme(theme_mode)
        #
        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton = True, showReturnButton = True)
        self.stackWidget = QStackedWidget(self)
        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.calenderInterface = Widget(self.tr('All-Plans View Interface'), self)
        self.folderInterface = Widget(self.tr('Classification Interface'), self)
        self.infoInterface = Widget(self.tr('Information Interface'), self)
        self.settingInterface = SettingInterface(self, self.setQss)
        # initialize layout
        self.initLayout()
        # add items to navigation interface
        self.initNavigation()
        # initialize Window Config
        self.initWindow()
    #
    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)
        #
        self.titleBar.raise_()
        self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)
    #
    def initNavigation(self):
        # enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)
        #
        # top
        # self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Serach')
        self.addSubInterface(self.homeInterface, FIF.HOME, self.tr('Today\'s Plan'))
        self.addSubInterface(self.calenderInterface, FIF.CALENDAR, self.tr('View All Plans'))
        #
        self.navigationInterface.addSeparator()
        #
        # center
        # add navigation items to scroll area
        self.addSubInterface(self.folderInterface, FIF.FOLDER, self.tr('Category 1'), NavigationItemPosition.SCROLL)
        #
        self.navigationInterface.addSeparator(position = NavigationItemPosition.BOTTOM)
        #
        # bottom
        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey = 'avatar',
            widget = AvatarWidget(),
            onClick = self.showMessageBox,
            position = NavigationItemPosition.BOTTOM
        )
        #
        self.navigationInterface.addSeparator(position = NavigationItemPosition.BOTTOM)
        #
        self.addSubInterface(self.infoInterface, FIF.INFO, self.tr('Information'), NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settingInterface, FIF.SETTING, self.tr('Setting'), NavigationItemPosition.BOTTOM)
        #
        #!IMPORTANT: don't forget to set the default route key
        qrouter.setDefaultRouteKey(self.stackWidget, self.homeInterface.objectName())
        #
        # set the maximum width
        # self.navigationInterface.setExpandWidth(300)
        #
        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(0)
    #
    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(grp('resource/logo.png')))
        self.setWindowTitle(self.tr('Yun · Schedule'))
        self.titleBar.setAttribute(Qt.WA_StyledBackground)
        #
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        #
        self.setQss()
    #
    def addSubInterface(self, interface, icon, text: str, position = NavigationItemPosition.TOP):
        ''' add sub interface '''
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey = interface.objectName(),
            icon = icon,
            text = text,
            onClick = lambda: self.switchTo(interface),
            position = position,
            tooltip = text
        )
    #
    def setQss(self):
        color = 'dark' if isDarkTheme() else 'light'
        font_id = QFontDatabase.addApplicationFont(grp('resource/number.ttf'))
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        with open(grp(f'resource/theme/{color}.qss'), encoding = 'utf-8') as qssFile:
            style = qssFile.read()
            self.setStyleSheet(style % font)
    #
    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)
    #
    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())
        qrouter.push(self.stackWidget, widget.objectName())
    #
    def showMessageBox(self):
        askSponsor = MessageBox(
            title = self.tr('Sponsored Author🥰'),
            content = self.tr('Personal development is not easy, if this project has helped you, \nconsider asking the author to drink a bottle of Coke🥤。\n\nYour support is the motivation for the author to develop and maintain the project🚀'),
            parent = self
        )
        askSponsor.yesButton.setText(self.tr('Sponsor!'))
        askSponsor.cancelButton.setText(self.tr('Next time~'))
        #
        if askSponsor.exec():
            QDesktopServices.openUrl(QUrl('https://afdian.net/a/lingyunawa'))
    #
    def resizeEvent(self, e):
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width()-46, self.titleBar.height())
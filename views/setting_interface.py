# coding:utf-8
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

from qfluentwidgets import (SettingCardGroup, ScrollArea, ExpandLayout, InfoBar, setTheme,
                            OptionsSettingCard, HyperlinkCard, PrimaryPushSettingCard)
from qfluentwidgets import FluentIcon as FIF

from common.Lib.g_config import cfg
from common.config import Constants

class SettingInterface(ScrollArea):
    """ Setting interface """
    def __init__(self, parent=None, QssEditFunction=None):
        super().__init__(parent=parent)
        # Get Qss EditFunction
        self.QssEditFunction = QssEditFunction
        #
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        # setting label
        self.settingLabel = QLabel(self.tr("Settings"), self)
        self.settingLabel.setContentsMargins(0, 20, 0, 0)
        # personalization
        self.personalGroup = SettingCardGroup(self.tr('Personalization'), self.scrollWidget)
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            self.tr('Application theme'),
            self.tr("Change the appearance of your application"),
            texts=[
                self.tr('Light'), self.tr('Dark'),
                self.tr('Use system setting')
            ],
            parent=self.personalGroup
        )
        # application
        self.aboutGroup = SettingCardGroup(self.tr('About'), self.scrollWidget)
        self.helpCard = HyperlinkCard(
            Constants.HELP_URL.value,
            self.tr('Open help page'),
            FIF.HELP,
            self.tr('Help'),
            self.tr('Discover new features and learn useful tips about Yun · Schedule'),
            self.aboutGroup
        )
        self.feedbackCard = HyperlinkCard(
            Constants.FEEDBACK_URL.value,
            self.tr('Provide feedback'),
            FIF.FEEDBACK,
            self.tr('Provide feedback'),
            self.tr('Help us improve Yun · Schedule by providing feedback'),
            self.aboutGroup
        )
        self.aboutCard = HyperlinkCard(
            Constants.RELEASE_URL.value,
            self.tr('Check update'),
            FIF.INFO,
            self.tr('About'),
            '© ' + self.tr('Copyright') + f" {Constants.YEAR.value}, {Constants.AUTHOR.value}. " +
            self.tr('Version') + " " + Constants.PACKAGE_VERSION.value,
            self.aboutGroup
        )
        self.__initWidget()
    #
    #
    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 100, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')
        # initialize style sheet
        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')
        # initialize layout
        self.__initLayout()
        self.__connectSignalToSlot()
    #
    def __initLayout(self):
        self.settingLabel.move(36, 30)
        # add cards to group
        self.personalGroup.addSettingCard(self.themeCard)
        self.aboutGroup.addSettingCards([self.helpCard, self.feedbackCard, self.aboutCard])
        # add setting card group to layout
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.personalGroup)
        self.expandLayout.addWidget(self.aboutGroup)
    #
    def __showRestartTooltip(self):
        """ show restart tooltip """
        InfoBar.success(
            self.tr('Updated successfully'),
            self.tr('Configuration takes effect after restart'),
            duration=1500,
            parent=self
        )
    #
    def __connectSignalToSlot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__showRestartTooltip)
        # personalization
        self.themeCard.optionChanged.connect(self.__settheme)

    def __settheme(self, ci):
        setTheme(cfg.get(ci))
        self.QssEditFunction()
# -*- coding:utf-8 -*-

from enum import Enum

from qfluentwidgets import isDarkTheme

from .resource import grp

class Icon(Enum):

    MOON = 'moon'

    def path(self):
        if isDarkTheme():
            return grp(f'resource/svg/{self.value}_dark.svg')
        else:
            return grp(f'resource/svg/{self.value}_light.svg')
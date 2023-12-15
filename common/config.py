# -*- coding:utf-8 -*-
from json import load, dump
from enum import Enum

class Config:
    def __init__(self, file_path = 'C:/ProgramData/YunSchedule/config/config.json'):
        self.file_path = file_path
        self.data = self.load_config()
        try:
            with open(self.file_path, 'x', encoding='utf-8') as f:
                pass
        except:
            pass

    def load_config(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return load(f)
        except FileNotFoundError:
            return {}

    def save_config(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            dump(self.data, f, ensure_ascii=False, indent=4)

    def getConfig(self, target):
        target = str(target)
        return self.data.get(target)

    def setConfig(self, target, value):
        target = str(target)
        value = str(value)
        self.data[target] = value
        self.save_config()

class Constants(Enum):
    YEAR = 2023
    AUTHOR = 'LingyunAwA'
    PACKAGE_VERSION = 'Beta 0.0.1'
    HELP_URL = 'https://github.com/LingyunAwA/YunSchedule/'

    def __str__(self):
        return self.value
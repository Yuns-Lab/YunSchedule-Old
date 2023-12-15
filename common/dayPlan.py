# -*- coding:utf-8 -*-
from json import load

from .config import Constants

default_path = Constants.DEFALUT_PATH.value

class Plan():
    def __init__(self, defaultPath: str | None = default_path) -> None:
        self.defaultPath = defaultPath

    def get1DayPlan(self, date: str):
        with open (f'{self.defaultPath}/{date}.json', "r") as file:
            plan = load(file.read)
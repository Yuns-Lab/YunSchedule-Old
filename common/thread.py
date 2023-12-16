from datetime import datetime

from PyQt5.QtCore import QThread, pyqtSignal

class TimeTitleUpdateThread(QThread):
    signal = pyqtSignal(str)
    #
    def __init__(self):
        super().__init__()
        self.TimeTitleUpdateThread_Status = True
    #
    def run(self):
        while self.TimeTitleUpdateThread_Status:
            now = datetime.now()
            dateStr = '现在是 {} 年 {} 月 {} 日 {} 时 {} 分 {} 秒'
            timeReplaceDict = {0:'00', 1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09'}
            hour = timeReplaceDict[now.hour] if now.hour < 10 else now.hour
            minute = timeReplaceDict[now.minute] if now.minute < 10 else now.minute
            second = timeReplaceDict[now.second] if now.second < 10 else now.second
            dateStr = dateStr.format(now.year, now.month, now.day, hour, minute, second)
            self.signal.emit(dateStr)
            self.sleep(1)
    #
    def stop(self):
        self.TimeTitleUpdateThread_Status = False
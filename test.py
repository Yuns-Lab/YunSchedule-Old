import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget

# 自定义线程类
class MyThread(QThread):
    # 定义信号，用于在线程中发送消息
    thread_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        # 线程执行的逻辑
        for i in range(5):
            message = "Message {}".format(i)
            self.thread_signal.emit(message)  # 发送信号
            self.sleep(1)  # 暂停一秒

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-threading Example")
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.label = QLabel("No message yet.")
        layout.addWidget(self.label)

        self.thread = MyThread()
        self.thread.thread_signal.connect(self.on_thread_message)  # 连接信号和槽函数

    def on_thread_message(self, message):
        self.label.setText(message)

    def start_thread(self):
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.start_thread()  # 启动多线程
    sys.exit(app.exec_())

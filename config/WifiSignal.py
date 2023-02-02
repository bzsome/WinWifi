from PyQt6 import QtCore
from PyQt6.QtCore import QObject


class WifiSignal(QObject):
    # 声明一个信号 只能放在函数的外面
    board_signal = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        pass

    def emit2(self, data):
        self.board_signal.emit(data)

    def connect(self, solt):
        self.board_signal.connect(solt)


board_signal = WifiSignal()


def testa(data):
    print(data.get("lan_ip"))
    print("---------")
    print(data.get("wan_ip"))


if __name__ == '__main__':
    board_signal.connect(testa)
    board_signal.emit2({"lan_ip": "a"})
    print("aaaaaa")

from PySide6.QtCore import QObject, Signal


class WifiSignal(QObject):
    # 声明一个信号 只能放在函数的外面
    board_signal = Signal(dict)

    def emit2(self, data):
        self.board_signal.emit(data)

    def connect2(self, solt):
        self.board_signal.connect(solt)


wifi_signal = WifiSignal()


def testa(data):
    print(data.get("lan_ip"))
    print("---------")
    print(data.get("wan_ip"))


if __name__ == '__main__':
    wifi_signal.connect2(testa)
    wifi_signal.emit2({"lan_ip": "a"})
    print("aaaaaa")

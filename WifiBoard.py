import sys

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QTextEdit, QTextBrowser, QMenu

import util.WifiScan
from config import WifiSignal


# wifi面板
class WifiBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        WifiSignal.wifi_signal.connect2(self.update_data)

    def init_ui(self):
        self.resize(400, 100)
        layout = QGridLayout()

        # 第1行
        self.wifi_textView = QTextBrowser(self)  # 调取文本浏览框显示文本内容
        self.wifi_textView.setText(" - 解决win11系统切换WiFi卡顿，切换慢的问题。支持记住Wifi密码，3-10秒完成WiFi的切换。")
        self.wifi_textView.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.wifi_textView.setMaximumHeight(28)
        layout.addWidget(self.wifi_textView, 0, 0, 1, 6)

        # 第2行
        button01 = QPushButton("当前WiFi：", self)
        layout.addWidget(button01, 1, 0)
        self.ssidText = QPushButton("-", self)
        layout.addWidget(self.ssidText, 1, 1, 1, 3)
        self.lanIpText = QPushButton("-", self)
        layout.addWidget(self.lanIpText, 1, 4, 1, 2)

        # 第4行
        button01 = QPushButton("公网IP：", self)
        layout.addWidget(button01, 2, 0)
        self.ipInfoText = QPushButton("-", self)
        layout.addWidget(self.ipInfoText, 2, 1, 1, 3)
        self.wanIpText = QPushButton("-", self)
        layout.addWidget(self.wanIpText, 2, 4, 1, 2)

        # 允许打开上下文菜单
        self.ssidText.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # 绑定事件
        self.ssidText.customContextMenuRequested.connect(self.generate_ssid_menu)
        self.setLayout(layout)

    def update_data(self, data):
        if data.get("ssid") is not None:
            self.ssidText.setText(data.get("ssid"))
        if data.get("lan_ip") is not None:
            self.lanIpText.setText(data.get("lan_ip"))
        if data.get("wan_ip") is not None:
            self.wanIpText.setText(data.get("wan_ip"))
        if data.get("wifi_text") is not None:
            self.wifi_textView.setText(data.get("(wifi_text"))
        if data.get("ip_info") is not None:
            self.ipInfoText.setText(data.get("ip_info"))

    def generate_ssid_menu(self, pos):
        menu = QMenu()
        item1 = menu.addAction("断开")

        # 转换坐标系
        screenPos = self.ssidText.mapToGlobal(pos)
        # 被阻塞
        action = menu.exec(screenPos)
        if action == item1:
            util.WifiScan.clear()
        else:
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WifiBoard()
    w.show()
    app.exec()

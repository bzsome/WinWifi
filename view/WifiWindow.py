# wifi窗口管理
import ctypes

from PySide6 import QtGui
from PySide6.QtGui import Qt
from PySide6.QtWidgets import *

from config import WifiSignal
from util import WifiScan
from view import WifiTable, WifiBoard

global wifi_window


class WifiWindow(QWidget):
    def __init__(self, parent=None):
        super(WifiWindow, self).__init__(parent)

        # 设置标题与初始大小
        self.setWindowTitle('Wifi快速连接工具')
        self.setWindowIcon(QtGui.QIcon('/docs/logo.ico'))
        self.resize(600, 600)

        # 设置布局
        layout = QVBoxLayout()

        self.wifi_board = WifiBoard.WifiBoard()
        layout.addWidget(self.wifi_board, stretch=1)

        self.wifi_table = WifiTable.WifiTable()
        layout.addWidget(self.wifi_table, stretch=4)

        self.setLayout(layout)


def check_wifi_interface():
    if WifiScan.get_iface() is None:
        WifiSignal.wifi_signal.emit2({"ssid": "找不到WiFi网卡，请连接WiFi网卡后重启程序"})
        QMessageBox.warning(None, '提示', '找不到WiFi网卡，请连接WiFi网卡后重启程序', QMessageBox.StandardButton.Yes)


def show_window():
    global wifi_window
    wifi_window = WifiWindow()
    # 设置任务图标
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DP
    wifi_window.setWindowIcon(QtGui.QIcon('/docs/logo.ico'))

    wifi_window.show()
    check_wifi_interface()


# 显示数据
def show_data(newWifiMap):
    wifi_window.wifi_table.show_data(newWifiMap)

# wifi窗口管理
import ctypes

from PySide6 import QtGui
from PySide6.QtGui import Qt
from PySide6.QtWidgets import *

import util.OsUtils
from config import WifiSignal
from util import WifiScan
from view import WifiTable, WifiBoard

global wifi_window


class WifiWindow(QWidget):
    def __init__(self, parent=None):
        super(WifiWindow, self).__init__(parent)

        # 设置标题与初始大小
        self.setWindowTitle('Wifi快速连接工具')
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

    set_icon(wifi_window)

    wifi_window.show()
    check_wifi_interface()


def set_icon(wifi_window):
    # 配置后显示任务栏图标
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    util.OsUtils.get_base_path()
    # 设置左上角图标
    ico_path = util.OsUtils.get_file_base_path('docs/logo.ico')
    print("ico_path:" + ico_path)
    wifi_window.setWindowIcon(QtGui.QIcon(ico_path))


# 显示数据
def show_data(newWifiMap):
    wifi_window.wifi_table.show_data(newWifiMap)

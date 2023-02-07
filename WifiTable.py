import time

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import *

from db import WifiDB
from util import WifiScan
from WifiBoard import WifiBoard

headers = ["热点SID", "型号强度", "加密方式"]

# ssid,signal,akm
rows = [["Newton", "80", "None"],
        ["Einstein", "70", "WPA2"],
        ["Darwin", "60", "WPA3"]]

global table, showWifiMap
showWifiMap = {}


class WifiTable(QWidget):
    def __init__(self, parent=None):
        super(WifiTable, self).__init__(parent)

        # 设置标题与初始大小
        self.setWindowTitle('Wifi快速连接工具')
        self.setWindowIcon(QtGui.QIcon('./docs/logo.ico'))
        self.resize(600, 600)
        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView()
        self.tableView.resize(600, 400)

        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(4, 4)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(headers)
        self.tableView.setModel(self.model)
        # 调整列宽（必须在setModel之后执行）
        self.tableView.setColumnWidth(0, 240)
        self.tableView.setColumnWidth(1, 100)
        self.tableView.setColumnWidth(2, 100)
        self.tableView.setColumnWidth(3, 100)

        # 允许打开上下文菜单
        self.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # 绑定事件
        self.tableView.customContextMenuRequested.connect(self.generate_menu)

        # 设置布局
        layout = QVBoxLayout()
        wifi_board = WifiBoard()
        layout.addWidget(wifi_board, stretch=1)
        layout.addWidget(self.tableView, stretch=4)
        self.setLayout(layout)

    def generate_menu(self, pos):
        # 获取点击行号
        for i in self.tableView.selectionModel().selection().indexes():
            rowNum = i.row()
        menu = QMenu()
        item1 = menu.addAction("连接")
        item2 = menu.addAction("属性")

        # 转换坐标系
        screenPos = self.tableView.mapToGlobal(pos)
        # 被阻塞
        action = menu.exec(screenPos)
        if action == item1:
            ssid = self.model.item(rowNum, 0).text()
            oldPwd = ""
            # 第三个参数表示显示类型，可选，有正常（QLineEdit.Normal）、密碼（ QLineEdit.Password）、不显示（ QLineEdit.NoEcho）三种情况
            oldWifi = WifiDB.get_wifi(ssid)
            if oldWifi.get("ssid") is not None:
                oldPwd = oldWifi.get("pwd")
            newPwd, ok = QInputDialog.getText(self, "连接 " + ssid, "请输入密码，无密码请留空:", text=oldPwd)
            if ok:
                WifiDB.update_wifi(ssid, newPwd)
                WifiScan.connect_wifi(ssid, newPwd)
        if action == item2:
            QMessageBox.information(None, '提示', '暂不支持', QMessageBox.StandardButton.Yes)
        else:
            return


def showApp():
    global table
    table = WifiTable()
    table.show()


# 显示数据
def showData(newWifiMap):
    global showWifiMap
    newWifiList = sort_wifi_list(list(newWifiMap.values()))
    table.model.setRowCount(len(newWifiList))
    for index, wifi in enumerate(newWifiList):
        item = QStandardItem(wifi.ssid)
        table.model.setItem(index, 0, item)

        item1 = QStandardItem(str(wifi.signal))
        table.model.setItem(index, 1, item1)

        item2 = QStandardItem(str(wifi.akm[0]))
        table.model.setItem(index, 2, item2)

    # 实时显示时间表示最后扫描时间
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    headers[0] = "热点SID (" + time_str + ")"
    table.model.setHorizontalHeaderLabels(headers)
    # 显示完成后保存当前显示的wifi数据
    showWifiMap = newWifiMap


def sort_wifi_list(wifiList):
    global showWifiMap
    # 设置排序默认值
    for wifiItem in wifiList:
        if not hasattr(wifiItem, 'preIndex'):
            wifiItem.preIndex = 0
    # 计算排序得分
    for wifiItem in wifiList:
        preIndex = get_wifi_pre_index(wifiItem.ssid)
        # 根据此算法，信号强度差距小于5，则不调整顺序
        wifiItem.sortScore = wifiItem.signal + (len(wifiList) - preIndex) * 5
    # 根据排序得分进行排序
    wifiList2 = sorted(wifiList, key=lambda wifi: wifi.sortScore, reverse=True)

    # 记录最新排序
    for index, wifiItem in enumerate(wifiList2):
        wifiItem.preIndex = index

    return wifiList2


# 获取展示的wifi次序
def get_wifi_pre_index(ssid):
    global showWifiMap
    showWifi = showWifiMap.get(ssid)
    if showWifi is None or not hasattr(showWifi, 'preIndex'):
        return 0
    else:
        return showWifi.preIndex

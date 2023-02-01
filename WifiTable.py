import time

from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import *

headers = ["热点SID", "型号强度", "加密方式"]

# ssid,signal,akm
rows = [["Newton", "80", "None"],
        ["Einstein", "70", "WPA2"],
        ["Darwin", "60", "WPA3"]]

global table


class Table(QWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        # 设置标题与初始大小
        self.setWindowTitle('QTableView表格视图的例子')
        self.resize(600, 400)
        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView()
        self.tableView.resize(600, 400)

        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(4, 4)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(headers)
        self.tableView.setModel(self.model)
        # 调整列宽（必须在setModel之后执行）
        self.tableView.horizontalHeader().resizeSection(0, 200)
        self.tableView.horizontalHeader().resizeSection(1, 100)
        self.tableView.horizontalHeader().resizeSection(2, 100)
        self.tableView.horizontalHeader().resizeSection(3, 100)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)


def showApp():
    global table
    table = Table()
    table.show()


def showData(ssidList):
    ssidList = sortWifiList(ssidList)
    table.model.setRowCount(len(ssidList))
    for index, wifi in enumerate(ssidList):
        item = QStandardItem(wifi.ssid)
        table.model.setItem(index, 0, item)

        item1 = QStandardItem(str(wifi.signal))
        table.model.setItem(index, 1, item1)

        item2 = QStandardItem(str(wifi.akm[0]))
        table.model.setItem(index, 2, item2)

    strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    headers[0] = "热点SID (" + strftime + ")"
    table.model.setHorizontalHeaderLabels(headers)


def sortWifiList(wifiList):
    return sorted(wifiList, key=lambda wifi: wifi.signal, reverse=True)

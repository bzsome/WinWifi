import time

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

headers = ["SID热点", "型号强度", "加密方式"]

# ssid,signal,akm
rows = [["Newton", "80", "None"],
        ["Einstein", "70", "WPA2"],
        ["Darwin", "60", "WPA3"]]

global view


class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)

    def columnCount(self, parent):
        return len(headers)

    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return headers[section]


def showApp():
    global view
    model = TableModel()
    view = QTableView()
    view.setModel(model)
    view.resize(600, 300)
    # 调整列宽
    view.horizontalHeader().resizeSection(0, 240)
    view.horizontalHeader().resizeSection(1, 120)
    view.horizontalHeader().resizeSection(2, 120)
    view.horizontalHeader().resizeSection(3, 120)
    view.show()


def showData(ssidList):
    ssidList = sortWifiList(ssidList)
    global rows, view
    # ssid,signal,akm
    rows = []
    for wifi in ssidList:
        rows.append([wifi.ssid, wifi.signal, wifi.akm[0]])

    model = TableModel()
    view.setModel(model)
    view.reset()


def sortWifiList(wifiList):
    return sorted(wifiList, key=lambda wifi: wifi.signal, reverse=True)

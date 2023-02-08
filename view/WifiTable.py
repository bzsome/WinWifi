# wifi列表展示
import time

from PySide6.QtGui import Qt, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QInputDialog, QMessageBox, QMenu, QTableView

from db import WifiDB
from util import WifiScan

global showWifiMap
showWifiMap = {}


class WifiTable(QTableView):
    def __init__(self, parent=None):
        super(WifiTable, self).__init__(parent)
        self.model = None
        self.init_view()

    def init_view(self):
        self.resize(600, 400)

        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(4, 4)
        self.headers = ["热点SID", "型号强度", "加密方式"]
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(self.headers)

        self.setModel(self.model)
        # 调整列宽（必须在setModel之后执行）
        self.setColumnWidth(0, 240)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 100)
        self.setColumnWidth(3, 100)

        # 允许打开上下文菜单
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # 绑定事件
        self.customContextMenuRequested.connect(self.generate_menu)

    def generate_menu(self, pos):
        # 获取点击行号
        for i in self.selectionModel().selection().indexes():
            rowNum = i.row()
        menu = QMenu()
        item1 = menu.addAction("连接")
        item2 = menu.addAction("属性")

        # 转换坐标系
        screenPos = self.mapToGlobal(pos)
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

    # 显示数据
    def show_data(self, newWifiMap):
        global showWifiMap
        newWifiList = sort_wifi_list(list(newWifiMap.values()))
        self.model.setRowCount(len(newWifiList))
        for index, wifi in enumerate(newWifiList):
            item = QStandardItem(wifi.ssid)
            self.model.setItem(index, 0, item)

            item1 = QStandardItem(str(wifi.signal))
            self.model.setItem(index, 1, item1)

            item2 = QStandardItem(str(wifi.akm[0]))
            self.model.setItem(index, 2, item2)

        # 实时显示时间表示最后扫描时间
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.headers[0] = "热点SID (" + time_str + ")"
        self.model.setHorizontalHeaderLabels(self.headers)
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

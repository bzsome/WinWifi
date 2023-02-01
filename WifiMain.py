# 继承QThread
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication

import WifiScan
import WifiTable

class Thread_1(QThread):  # 线程1
    def run(self):
        while True:
            wifiList = WifiScan.scan_wifi(1)
            ssidList = []
            for ssid in wifiList:
                ssidList.append(wifiList[ssid])
            WifiTable.showData(ssidList)


app = QApplication([])
WifiTable.showApp()
t1 = Thread_1()
t1.start()
app.exec()

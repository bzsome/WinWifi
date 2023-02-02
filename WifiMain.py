# 继承QThread
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication

import WifiScan
import WifiTable


class ScanThread(QThread):  # 线程1
    def run(self):
        while True:
            wifiMap = WifiScan.scan_wifi(1)
            WifiTable.showData(wifiMap)


app = QApplication([])
WifiTable.showApp()
t1 = ScanThread()
t1.start()
app.exec()

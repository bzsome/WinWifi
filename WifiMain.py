# 继承QThread
import time
import traceback

from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication

import WifiScan
import WifiTable


class ScanThread(QThread):  # 线程1
    def run(self):
        while True:
            try:
                wifiMap = WifiScan.scan_wifi(0.9)
                WifiTable.showData(wifiMap)
            except Exception as e:
                traceback.print_exc()
                print("scan_wifi failed", e)
            finally:
                time.sleep(0.1)


app = QApplication([])
WifiTable.showApp()
t1 = ScanThread()
t1.start()
app.exec()

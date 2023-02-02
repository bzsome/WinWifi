# 继承QThread
import socket
import time
import traceback

from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication

import WifiScan
import WifiTable
from config import WifiSignal
from util import IpUtil


# WiFi实时扫描
class ScanThread(QThread):
    def run(self):
        wifiMap = WifiScan.scan_wifi(0.1)
        WifiTable.showData(wifiMap)
        while True:
            try:
                wifiMap = WifiScan.scan_wifi(0.9)
                WifiTable.showData(wifiMap)
            except Exception as e:
                traceback.print_exc()
                print("scan_wifi failed", e)
            finally:
                time.sleep(0.1)


# 监控Wifi状态
class WifiStatusThread(QThread):
    def run(self):
        while True:
            try:
                wifiStatus = WifiScan.get_wifi_status()
                if wifiStatus is not None and len(wifiStatus) >= 1:
                    WifiSignal.board_signal.emit2({"ssid": wifiStatus[0].ssid})
            except Exception as e:
                traceback.print_exc()
                print("get_wifi_status failed", e)
            finally:
                time.sleep(1)


# 监控局域网IP
class LanIPStatusThread(QThread):
    def run(self):
        while True:
            try:
                time.sleep(0.8)
                lan_ip = IpUtil.get_lan_ip()
                WifiSignal.board_signal.emit2({"lan_ip": lan_ip})
            except Exception as e:
                traceback.print_exc()
                print("get_lan_ip failed", e)
            finally:
                time.sleep(10)


# 监控公网IP状态
class IpInfoThread(QThread):
    def run(self):
        while True:
            try:
                location = IpUtil.get_location()
                ip_info = "{_city}/{_region} ({_org})".format(_city=location.get("city"),
                                                              _region=location.get("region"),
                                                              _org=location.get("org"))
                WifiSignal.board_signal.emit2({"wan_ip": location.get("ip"), "ip_info": ip_info})
            except Exception as e:
                traceback.print_exc()
                print("get_ip failed", e)
            finally:
                time.sleep(60 * 10)


def start_thread():
    t1 = ScanThread()
    t1.start()
    t2 = WifiStatusThread()
    t2.start()
    t3 = IpInfoThread()
    t3.start()
    t4 = LanIPStatusThread()
    # TODO 获取会导致程序退出，原因未知
    # t4.start()

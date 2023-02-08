# 多线程控制类，定时扫描等任务
import threading
import time
import traceback

from config import WifiSignal
from util import IpUtil, WifiScan
from util.timer import RepeatingTimer
from view import WifiWindow

global timers


# WiFi实时扫描
def update_wifi_list():
    try:
        wifiMap = WifiScan.scan_wifi(0.1)
        if wifiMap is not None:
            WifiWindow.show_data(wifiMap)
    except Exception as e:
        traceback.print_exc()
        print("scan_wifi failed", e)


# 监控Wifi状态
def update_wifi_status():
    if WifiScan.get_iface() is None:
        return
    try:
        wifiStatus = WifiScan.get_wifi_status()
        if wifiStatus is not None and len(wifiStatus) >= 1:
            WifiSignal.wifi_signal.emit2({"ssid": wifiStatus[0].ssid})
    except Exception as e:
        traceback.print_exc()
        print("get_wifi_status failed", e)
    finally:
        time.sleep(1)


# 监控局域网IP
def update_lan_ip():
    try:
        time.sleep(0.8)
        lan_ip = IpUtil.get_lan_ip()
        WifiSignal.wifi_signal.emit2({"lan_ip": lan_ip})
    except Exception as e:
        traceback.print_exc()
        print("get_lan_ip failed", e)
    finally:
        time.sleep(10)


# 监控公网IP信息
def update_ip_info():
    try:
        location = IpUtil.get_location()
        if location.get("errMsg") is not None:
            ip_info = location.get("errMsg")
        else:
            ip_info = "{_city}/{_region} ({_org})".format(_city=location.get("city"),
                                                          _region=location.get("region"),
                                                          _org=location.get("org"))
        WifiSignal.wifi_signal.emit2({"wan_ip": location.get("ip"), "ip_info": ip_info})
    except Exception as e:
        traceback.print_exc()
        print("get_ip failed", e)


def start_thread():
    global timers
    timers = []
    # 创建子线程对象
    thread_obj1 = threading.Thread(target=update_wifi_list)
    # 启动子线程对象
    thread_obj1.start()
    timer1 = RepeatingTimer(1, update_wifi_list)
    timer1.start()
    timers.append(timer1)

    # 创建子线程对象
    thread_obj2 = threading.Thread(target=update_wifi_status)
    # 启动子线程对象
    thread_obj2.start()
    timer2 = RepeatingTimer(10, update_wifi_status)
    timer2.start()
    timers.append(timer2)

    # 创建子线程对象
    thread_obj3 = threading.Thread(target=update_ip_info)
    # 启动子线程对象
    thread_obj3.start()
    timer3 = RepeatingTimer(60, update_ip_info)
    timer3.start()
    timers.append(timer3)

    # 创建子线程对象
    thread_obj4 = threading.Thread(target=update_lan_ip)
    # 启动子线程对象
    thread_obj4.start()
    timer4 = RepeatingTimer(5, update_lan_ip)
    timer4.start()
    timers.append(timer4)


def stop_thread():
    for timer in timers:
        timer.cancel()

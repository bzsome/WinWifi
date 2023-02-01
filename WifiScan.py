import time

import pywifi

global iface
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]


def scan_wifi(timeout=1):
    global iface
    """扫描可用wifi"""
    wifiMap = {}
    print('start to scan ssid, wait {}s'.format(timeout))
    iface.scan()
    time.sleep(timeout)
    result = iface.scan_results()
    if result is None:
        return []

    for newWifi in result:
        newSsid = newWifi.ssid.encode('raw_unicode_escape').decode('utf-8')
        newWifi.ssid = newSsid
        oldWifi = wifiMap.get(newSsid)
        if oldWifi is not None:
            # 已存在的情况,型号强度更强的才替换
            if newWifi.signal > oldWifi.signal:
                wifiMap[oldWifi.ssid] = oldWifi
        else:
            wifiMap[newSsid] = newWifi

    return wifiMap

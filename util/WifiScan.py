import time

import pywifi

global iface, scanWifiMap
wifi = pywifi.PyWiFi()
global iface
iface = None
scanWifiMap = {}


def get_iface():
    global iface
    if iface is None:
        interfaces = wifi.interfaces()
        if len(interfaces) >= 1:
            iface = interfaces[0]
    return iface


def scan_wifi(timeout=1):
    if get_iface() is None:
        return
    global scanWifiMap
    """扫描可用wifi"""
    wifiMapTemp = {}
    get_iface().scan()
    time.sleep(timeout)
    result = get_iface().scan_results()
    if result is None:
        return {}

    for newWifi in result:
        newSsid = newWifi.ssid.encode('raw_unicode_escape').decode('utf-8')
        newWifi.ssid = newSsid
        oldWifi = wifiMapTemp.get(newSsid)
        if oldWifi is not None:
            # 已存在的情况,型号强度更强的才替换
            if newWifi.signal > oldWifi.signal:
                wifiMapTemp[oldWifi.ssid] = oldWifi
        else:
            wifiMapTemp[newSsid] = newWifi
    scanWifiMap = wifiMapTemp
    return wifiMapTemp


def connect_wifi(ssid, pwd):
    if get_iface() is None:
        return
    global scanWifiMap
    sWifi = scanWifiMap.get(ssid)
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.key = pwd
    profile.akm = sWifi.akm
    profile.auth = sWifi.auth
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP

    """清除所有网络连接"""
    get_iface().remove_all_network_profiles()
    time.sleep(0.1)

    temp_profile = get_iface().add_network_profile(profile)
    get_iface().connect(temp_profile)


def get_wifi_status():
    if get_iface() is None:
        return
    return get_iface().network_profiles()


def clear():
    if get_iface() is None:
        return
    """清除所有网络连接"""
    get_iface().remove_all_network_profiles()
    time.sleep(0.1)

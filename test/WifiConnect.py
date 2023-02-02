import time

import pywifi

profile = pywifi.Profile()
profile.ssid = "GT NEO 3"
profile.key = "12345678a"
profile.akm = [pywifi.const.AKM_TYPE_WPA2PSK]
profile.auth = pywifi.const.AUTH_ALG_OPEN
profile.cipher = pywifi.const.CIPHER_TYPE_CCMP

wifi = pywifi.PyWiFi()
# choose wifi interface
iface = wifi.interfaces()[0]

"""清除所有网络连接"""
iface.remove_all_network_profiles()
time.sleep(0.1)

temp_profile = iface.add_network_profile(profile)
iface.connect(temp_profile)

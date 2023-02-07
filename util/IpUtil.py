import socket
import traceback

import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    try:
        response = requests.get('https://ipapi.co/json/')
    except Exception as e:
        traceback.print_exc()
        print(e)
        return {}
    response = response.json()
    location_data = {
        "ip": response.get("ip"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "org": response.get("org")
    }
    return location_data


# 获取局域网IP
def get_lan_ip():
    try:
        # socket.SOCK_DGRAM代表的是socket使用UDP协议进行通讯
        # 除此之外socket.SOCK_STREAM使用的是TCP协议进行通讯
        skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        skt.connect(("8.8.8.8", 80))  # 谷歌公共DNS 地址，端口任意填
        lan_ip = skt.getsockname()[0]
        return lan_ip
    except Exception as e:
        print(e)
    finally:
        skt.close()


def get_lan_ip2():
    hostname, alias_list, ipaddr_list = socket.gethostbyname(socket.gethostname())
    print(hostname)
    print(alias_list)
    print(ipaddr_list)


if __name__ == '__main__':
    location = get_lan_ip()
    print(location)

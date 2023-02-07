import os
import sqlite3
from datetime import datetime

global cursor, connection
# 数据库存储目录
db_dir = os.environ['USERPROFILE'] + "/bzchao/PyWifi"
# 数据库文件名
db_name = "wifi.db"

global connection, cursor


def create_wifi_table():
    try:
        create_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS wifi_pwd(
            ssid varchar(255), 
            pwd varchar(255), 
            akm varchar(64),
            create_time datetime,
            update_time datetime
            )
          '''
        connection.execute(create_tb_cmd)
        connection.commit()
        return True
    except Exception as e:
        print("Create table failed", e)
        return False


def get_wifi(ssid):
    global cursor
    res = cursor.execute("SELECT ssid, pwd, akm,create_time,update_time from wifi_pwd where ssid = ?", (ssid,))
    wifi = {}
    for row in res:
        wifi["ssid"] = row[0]
        wifi["pwd"] = row[1]
        wifi["akm"] = row[2]
        wifi["create_time"] = row[3]
        wifi["update_time"] = row[4]
    return wifi


def update_wifi(ssid, pwd):
    global cursor
    wifi = get_wifi(ssid)
    if wifi.get("ssid") is None:
        cursor.execute("insert into wifi_pwd (ssid,pwd,create_time) values (?,?,?)", (ssid, pwd, datetime.now()))
    else:
        cursor.execute("update wifi_pwd set pwd=?,update_time=? where ssid = ?", (pwd, datetime.now(), ssid))
    connection.commit()


def init_db():
    global connection, cursor
    os.makedirs(db_dir, exist_ok=True)
    connection = sqlite3.connect(db_dir + "/" + db_name)
    cursor = connection.cursor()
    create_wifi_table()


if __name__ == '__main__':
    init_db()
    update_wifi("gtneo", "12345678")
    wifi = get_wifi("gtneo")
    print(wifi)

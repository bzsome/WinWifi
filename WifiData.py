import sqlite3

global cursor, connection
connection = sqlite3.connect("wifi.db")
cursor = connection.cursor()

print("数据插入成功")
cursor = cursor.execute("SELECT ssid, pwd, akm from wifi_pwd")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2], "\n")


def get_wifi(ssid):
    global cursor
    res = cursor.execute("SELECT ssid, pwd, akm from wifi_pwd where ssid = ?", ssid)
    wifi = {}
    for row in res:
        wifi["ssid"] = row[0]
        wifi["pwd"] = row[1]
        wifi["akm"] = row[2]


def update_wifi(ssid, pwd, akm):
    global cursor
    cursor.execute("update wifi_pwd set pwd=?,akm=? where ssid = ?", (pwd, akm, ssid))
    connection.commit()

import sys

from PyQt6.QtWidgets import QApplication

import WifiTable
import WifiThread
from db import WifiDB

app = QApplication([])
WifiDB.init_db()
print("showApp()")
WifiTable.showApp()
print("start_thread()")
WifiThread.start_thread()
try:
    print("exec()")
    app.exec()
except Exception as e:
    print(e)

WifiThread.stop_thread()
print("exit()")
sys.exit(0)

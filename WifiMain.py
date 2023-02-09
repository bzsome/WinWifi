import sys

from PySide6.QtWidgets import QApplication

import WifiThread
from db import WifiDB
from view import WifiWindow

app = QApplication([])

WifiDB.init_db()
print("show_window()")
WifiWindow.show_window()
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

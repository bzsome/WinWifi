import ctypes
import sys

from PySide6 import QtGui
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication

import WifiTable
import WifiThread
from db import WifiDB

app = QApplication([])
# 设置任务图标
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DP
app.setWindowIcon(QtGui.QIcon('/docs/logo.ico'))

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
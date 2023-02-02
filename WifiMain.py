from PyQt6.QtWidgets import QApplication

import WifiTable
import WifiThread

app = QApplication([])
print("showApp()")
WifiTable.showApp()
print("start_thread()")
WifiThread.start_thread()
print("exec()")
try:
    app.exec()
except Exception as e:
    print(e)

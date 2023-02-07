from PySide6.QtWidgets import *
from PySide6.QtCore import *

headers = ["SID热点", "型号强度", "加密方式"]

rows = [("Newton", "80", "None"),
        ("Einstein", "70", "WPA2"),
        ("Darwin", "60", "WPA3")]


class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)

    def columnCount(self, parent):
        return len(headers)

    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return headers[section]


app = QApplication([])
model = TableModel()
view = QTableView()
view.setModel(model)
view.resize(600, 300)
# 调整列宽
view.horizontalHeader().resizeSection(0, 120)
view.horizontalHeader().resizeSection(0, 120)
view.horizontalHeader().resizeSection(0, 120)
view.horizontalHeader().resizeSection(0, 120)

view.show()
app.exec()

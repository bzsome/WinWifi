import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QMenu, QVBoxLayout

'''
在 QTableWidget 表格中实现右键快捷菜单 的案例
1.如何弹出菜单
2.如何在满足条件的情况下弹出菜单
QMenu.exec_
'''


class twContextDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置定位和左上角坐标
        self.setGeometry(300, 300, 460, 360)
        # 设置窗口标题
        self.setWindowTitle('QTableWidget扩展表格显示上下文菜单 的演示')
        # 设置窗口图标
        # self.setWindowIcon(QIcon('../web.ico'))

        layout = QVBoxLayout()
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(3)
        self.tablewidget.setColumnCount(3)

        layout.addWidget(self.tablewidget)
        self.tablewidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        newItem = QTableWidgetItem('美国队长')
        self.tablewidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('男')
        self.tablewidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('180')
        self.tablewidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem('拿破仑')
        self.tablewidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem('女')
        self.tablewidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem('150')
        self.tablewidget.setItem(1, 2, newItem)

        # 允许打开上下文菜单
        self.tablewidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # 绑定事件
        self.tablewidget.customContextMenuRequested.connect(self.generateMenu)

        self.setLayout(layout)

    def generateMenu(self, pos):
        print(pos)

        # 获取点击行号
        for i in self.tablewidget.selectionModel().selection().indexes():
            rowNum = i.row()
        # 如果选择的行索引小于2，弹出上下文菜单
        if rowNum < 2:
            menu = QMenu()
            item1 = menu.addAction("复制")
            item2 = menu.addAction("剪切")
            item3 = menu.addAction("粘贴")
            item4 = menu.addAction("添加一行")
            item5 = menu.addAction("删除")
            item6 = menu.addAction("修改")

            # 转换坐标系
            screenPos = self.tablewidget.mapToGlobal(pos)
            print(screenPos)

            # 被阻塞
            action = menu.exec(screenPos)
            if action == item1:
                print('选择了第1个菜单项', self.tablewidget.item(rowNum, 0).text()
                      , self.tablewidget.item(rowNum, 1).text()
                      , self.tablewidget.item(rowNum, 2).text())
            elif action == item2:
                print('选择了第2个菜单项', self.tablewidget.item(rowNum, 0).text()
                      , self.tablewidget.item(rowNum, 1).text()
                      , self.tablewidget.item(rowNum, 2).text())
            elif action == item3:
                print('选择了第3个菜单项', self.tablewidget.item(rowNum, 0).text()
                      , self.tablewidget.item(rowNum, 1).text()
                      , self.tablewidget.item(rowNum, 2).text())
            elif action == item4:
                print('选择了第4个菜单项', self.tablewidget.item(rowNum, 0).text()
                      , self.tablewidget.item(rowNum, 1).text()
                      , self.tablewidget.item(rowNum, 2).text())
            else:
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置应用图标
    app.setWindowIcon(QIcon('../web.ico'))
    w = twContextDemo()
    w.show()
    app.exec()

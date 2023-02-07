import sys
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        layout = QGridLayout()
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"]
        }
        for line_num, temp_data in data.items():
            for col_num, tp in enumerate(temp_data):
                print(tp)
                btn = QPushButton(tp)
                # 将按钮添加到第几行第几个
                layout.addWidget(btn, line_num, col_num)
        self.setLayout(layout)


# 在窗口中添加格子按钮，使得与输入的data位置对应
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()

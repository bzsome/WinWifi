from PySide6.QtCore import QObject, Signal


# 信号对象
class CustomSignal(QObject):
    # 定义一个信号
    signal_send_msg = Signal(dict)


def get_msg2(msg1):
    print("QSlot get msg => ", msg1)


if __name__ == '__main__':
    custom_signal = CustomSignal()  # 实例化信号对象
    # 把信号绑定到槽函数上
    custom_signal.signal_send_msg.connect(get_msg2)
    custom_signal.signal_send_msg.emit({"a": '第一参数', "b": '第二个参数'})

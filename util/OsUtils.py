import os
import sys
import webbrowser


def get_base_path():
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        # 单个exe解药后的路径
        base_path = sys._MEIPASS
    elif "NUITKA_ONEFILE_PARENT" in os.environ:
        # 使用NUITKA打包
        # base_path = os.path.dirname(__file__) //这个路径无法在其它程序中打开
        base_path = os.path.dirname(sys._base_executable)
    else:
        # 不打包，正常执行的路径
        base_path = os.path.abspath(".")
    return base_path


def get_file_base_path(file):
    return os.path.join(get_base_path(), file)


# 此处必须注意，绑定的事件函数中必须要包含event参数
def open_url(event):
    webbrowser.open("https://github.com/bzsome", new=0)

# PyWifi

wifi连接工具，快速连接wifi，解决widow11系统切换wifi慢的问题

## 功能说明

- 实时扫描可用Wifi列表

- 连接后记住密码功能

- 根据信号强度排序显示

    - 为防止列表变动过快，通过算法（信号强度+之前次序）进行排序，与前一名得分差距不大的情况下，不调整显示顺序

- 显示已连接Wifi，公网IP信息

## 打包

参照教程：https://zhuanlan.zhihu.com/p/133303836

- 打包命令：

nuitka --standalone --disable-console ^
--plugin-enable=pyqt6 ^
--include-package=chardet ^
--output-dir=out ^
WifiMain.py
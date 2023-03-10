# WinWifi

wifi连接工具，快速连接wifi，解决widow11系统切换wifi慢的问题

## 直接下载程序

- wifi连接工具Windows版： [WinWifi_1.0.exe](https://github.com/bzsome/WinWifi/releases/download/v1.0/WinWifi_1.0.exe)

## 运行效果图

- 程序主界面（windows）

<img src="./docs/wifi_screen.png" width="50%" height="50%" alt="程序运行图windows" align="center" />

## 功能说明

- 实时扫描可用Wifi列表

- 连接后记住密码功能

- 根据信号强度排序显示

    - 为防止列表变动过快，通过算法（信号强度+之前次序）进行排序，与前一名得分差距不大的情况下，不调整显示顺序

- 显示已连接Wifi，公网IP信息

## 发布打包

参照教程：https://zhuanlan.zhihu.com/p/133303836

- 打包命令：

    - 发布打包：build.bat 不显示控制台，压缩可执行文件
    - 测试打包：dev.bat 显示控制台，不进行压缩

- 打包结果：

nuitka打包约后19.3M

## 问题记录

### 打包后无法显示任务栏图标

- 主要原因1：打包后资源文件在tmp目录。程序无法正常获取到tmp目录下的文件

- 主要原因2：内置属性__file__只能获取一个临时的路径，且只有当前程序能够访问

  图标由系统设置，需要给系统一个非本程序也能访问的地址

- 解决方案：通过遍历sys中的所有属性，发现可以使用sys._base_executable获取真正的临时目录

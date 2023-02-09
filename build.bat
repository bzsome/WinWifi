nuitka --standalone --onefile --disable-console ^
--full-compat ^
--windows-icon-from-ico=./docs/logo.ico ^
--include-data-file=./docs/*=./docs/ ^
--plugin-enable=pyside6,upx ^
--include-package=chardet ^
--output-dir=out ^
WifiMain.py
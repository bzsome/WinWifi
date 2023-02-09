nuitka --standalone --onefile ^
--windows-icon-from-ico=./docs/logo.ico ^
--include-data-file=./docs/*=./docs/ ^
--plugin-enable=pyside6 ^
--include-package=chardet ^
--output-dir=out ^
--run ^
WifiMain.py
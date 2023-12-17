cls
color b
@echo off
@echo Build Log:
@echo.

E:/Linguist_v6.6.1/lrelease.exe resource/i18N/zh_CN.ts -qm resource/i18N/zh_CN.qm

:: delay exit
ping 127.0.0.1 -n 6 > nul
color
cls
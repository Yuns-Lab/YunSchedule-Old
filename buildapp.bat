@echo off

:: start display
cls
color c
@echo -------------------------------------------------------------------
@echo -              Start to building app via app.spec                 -
@echo -------------------------------------------------------------------
ping 127.0.0.1 -n 6 > nul

cls
color f

:: reset output folder
rd /s /q "dist\"
mkdir "dist"

:: build display
cls
color b
@echo -------------------------------------------------------------------
@echo -                          Building Begin                         -
@echo -           Please do not torch anything, log is under here       -
@echo -------------------------------------------------------------------
@echo.
@echo.
ping 127.0.0.1 -n 4 > nul

:: pyinstaller building
@echo Build Log:
@echo.
pyinstaller app.spec

:: dealy for checking logs, CLS after
ping 127.0.0.1 -n 11 > nul

:: remove build folders
rd /s /q "build\app\"
rd /s /q "build\app\"
rd /s /q "build\"
rd /s /q "build\"

:: end display
cls
color a
@echo -------------------------------------------------------------------
@echo -                           Build Finish                          -
@echo -------------------------------------------------------------------

:: delay exit
ping 127.0.0.1 -n 6 > nul
color
cls
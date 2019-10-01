title Generador de EXE
@echo off
:: Header to show in the screen. 
cls

@echo _________________________________________________________
@echo.
@echo     ##                       #             ### # # ### 
@echo    #   ### ##  ### ###  ## ### ### ###     #   # # #   
@echo    # # ##  # # ##  #   # # # # # # #       ##   #  ##  
@echo    # # ### # # ### #   ### ### ### #       #   # # #   
@echo     ##                                     ### # # ### 
@echo _________________________________________________________
@echo.
@echo     Name:        GeneracionExe.bat
@echo     Version:     1.0
@echo     Description: Software to generate the executable of
@echo                  the TestChecker application 
@echo     Author:      Juan Bueno 
@echo     Date:        26/11/2018 
@echo _________________________________________________________
@echo.
@echo off


:: Check for python 2.7 installation.
if exist c:\Python27\python.exe goto CheckPy2exe
@echo on
@echo ERROR!!! The Python 2.7 has not been found!!!
@echo The script going to be stopped... 
@echo off
pause
exit


:: Check for py2exe installation.
:CheckPy2exe
if exist C:\Python27\Lib\site-packages\py2exe\run.exe goto GeneracionExe
@echo on
@echo ERROR!!! The Py2Exe has not been found!!!
@echo The script going to be stopped... 
@echo off
pause
exit


:: Execution of the scripts to generate the executable. 
:GeneracionExe
call c:\Python27\python.exe setup.py install
call c:\Python27\python.exe setup.py py2exe -d "TestChecker"
if errorlevel 0 goto CompleteDistro

:: Aditional stuff for TestChecker application.
:CompleteDistro
xcopy /b/v/y logos TestChecker\logos\
xcopy /b/v/y CSS TestChecker\CSS\
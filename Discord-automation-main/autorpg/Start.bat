@echo off

echo Downloading libraries...
pip install pyautogui
cls
pip install art
cls
pip install colorama
cls
pip install progressbar
cls


echo Libraires installed...
echo starting main script...
cls



set "dir=%~dp0commands\"

for %%f in ("%dir%*.py") do (
    set "filename=%%~nf"
    start "Python Script - !filename!" python "%%~ff"
)


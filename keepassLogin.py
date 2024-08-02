import os
import pyautogui
import subprocess
import time
import pygetwindow
from dotenv import load_dotenv

env_path = "./variables.env"

load_dotenv(dotenv_path=env_path)

with open(env_path, 'r') as file:
    password = os.getenv("PASSWORD")
    keepassxc_executable = os.getenv("KEEPASSXC_EXECUTABLE")
if not password:
    print('Failed to parse file')
    exit(1)

subprocess.Popen([keepassxc_executable])
print("Launched KeePassXC")

time.sleep(3)

try:
    expected_window_title = "KeePassXC"
    window = pygetwindow.getWindowsWithTitle(expected_window_title)[0]
    if not window:
        print('Failed to find window')
        exit(2)
    
    window.activate()
    time.sleep(1)
    
    for char in password:
        focused_window = pygetwindow.getActiveWindow()
        if focused_window and expected_window_title in focused_window.title:
            pyautogui.typewrite(char, interval=0.1)
            
        else: 
            print('KeePassXC Window lost focus, refocusing...')
            window.activate()
            time.sleep(0.5)
            pyautogui.typewrite(char, interval=0.1)
        
    pyautogui.press('enter')

except Exception as e: 
    print(f'Failed to open the database {e}')

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
    else:
        focused_window = pygetwindow.getActiveWindow()
        if focused_window and expected_window_title in focused_window.title:
            window.activate();
            pyautogui.typewrite(password, interval=0.025)
            pyautogui.press('enter')
            print("Database unlocked successfully!")
        else: 
            print('No window with KeePassXC detected')
            exit(2)
        
except Exception as e: 
    print(f'Failed to open the database {e}')

input("Press any key to exit")
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

if not password and not keepassxc_executable:
    print('Variables in the variables.env file need to be filled in first.')
    input('Press any key to exit')
    exit();

if not password:
    print('Password is missing from the variables.env file. \nPlease enter your password in the specified variable field e.g: PASSWORD = "P@ssword"')
    input('Press any key to exit')
    exit();

if not keepassxc_executable: 
    print('KeePassXC variable has not beeen defined, please fill in the path to KeePassXC along with KeePassXC.exe in the variables.env file. \ne.g: "C:\\Program Files\\KeePassXC\\KeePassXC.exe"')
    input('Press any key to exit')
    exit();
    
subprocess.Popen([keepassxc_executable])
print("Launching KeePassXC...")

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
                pyautogui.typewrite(char)
                
            else: 
                print('KeePassXC Window lost focus, refocusing...')
                window.activate()
                time.sleep(0.5)
                pyautogui.typewrite(char)
            
        pyautogui.press('enter')

except Exception as e: 
    print(f'Failed to open the database {e}')
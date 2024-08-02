# KeePassXC Auto Login
A simple auto-login solution for those who don't want to type in their password manually every time the application boots up.


## Installation
- Extract the contents of the archived file.  
- Execute **install_dependencies.bat**


<h2 style="color: red">Important</h2>



Navigate to the root folder where the **run_auto_login.bat** file is located.

Open the **variables.env** file with your favorite text editor (notepad works).  

Assign the location of KeePassXC's executable and the password to the variables

```
KEEPASSXC_EXECUTABLE = ""
PASSWORD = ""
```
### Example
```
KEEPASSXC_EXECUTABLE = "C:\Program Files\KeePassXC\KeePassXC.exe"
PASSWORD = "P@ssword"
```

## How to use
After the dependencies have been installed, you can create a startup shortcut for Windows and place it in your Windows startup folder for it to automatically open KeePassXC for you and exectute the login process. 

- Create a shortcut of **run_auto_login.bat**
- Press Win+r and type ``` shell:startup ``` and paste the shortcut in that folder. 

That's it. It should target KeePassXC's window and fill in the password field. 

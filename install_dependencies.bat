@echo off
REM Create virtual environment if it doesn't exist
if not exist .venv (
    python -m venv .venv
    echo Virtual environtment created
)

REM Activate the virtual environment
call .venv\Scripts\activate

REM Install dependencies within the virtual environment
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Press any key to exit...
pause >nul
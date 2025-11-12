@echo off

if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    call .venv\Scripts\activate.bat
)

del /f /q "download\version_manifest.json" >nul 2>&1

echo Running the main script...
python src\main.py

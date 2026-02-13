@echo off
REM One-click runner for Windows (cmd)
REM Creates venv if missing, installs requirements, seeds DB, and runs app
SET LESSON_DIR=%~dp0
IF NOT EXIST "%LESSON_DIR%venv\Scripts\python.exe" (
    echo Creating venv in lesson folder...
    python -m venv "%LESSON_DIR%venv"
)
call "%LESSON_DIR%venv\Scripts\activate.bat"
pip install -r "%LESSON_DIR%requirements.txt"
python "%LESSON_DIR%seed_demo.py"
echo Starting Flask app...
python "%LESSON_DIR%run.py"
pause

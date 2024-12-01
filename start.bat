@echo off
echo Activating virtual environment...
call .\venv\Scripts\activate

echo Running the Python application...
python app/main.py >> G:\My Drive\logs\logs.txt 2>&1

echo Application has finished running.
pause

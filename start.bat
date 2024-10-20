@echo off
echo Activating virtual environment...
call .\venv\Scripts\activate

echo Running the Python application...
python app/main.py >> logs.txt 2>&1

echo Application has finished running. Check logs.txt for output.
pause

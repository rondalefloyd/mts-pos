@echo off
:: Set the variables for database connection and backup folder
set PGUSER=postgres
set PGPASSWORD=admin
set PGHOST=localhost
set PGPORT=5432
set PGDATABASE=postgres
set BACKUP_DIR=G:\My Drive\backups

:: Create the backup directory if it doesn't exist
if not exist "%BACKUP_DIR%" (
    mkdir "%BACKUP_DIR%"
)

:: Get the current timestamp
for /f "tokens=1-4 delims=/- " %%a in ("%date%") do (
    set YEAR=%%c
    set MONTH=%%a
    set DAY=%%b
)
for /f "tokens=1-3 delims=:. " %%a in ("%time%") do (
    set HOUR=%%a
    set MINUTE=%%b
    set SECOND=%%c
)

:: Format the timestamp (adjust as needed)
set TIMESTAMP=%YEAR%-%MONTH%-%DAY%_%HOUR%-%MINUTE%-%SECOND%

:: Create a backup using pg_dump
pg_dump -h %PGHOST% -p %PGPORT% -U %PGUSER% -F c -b -v -f "%BACKUP_DIR%\backup_%TIMESTAMP%.sql" %PGDATABASE%

:: Optional: Clean up old backups (keep only last 10)
for /f "skip=10 delims=" %%f in ('dir /b /o-d "%BACKUP_DIR%\backup_*.sql"') do del "%BACKUP_DIR%\%%f"

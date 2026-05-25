@echo off
setlocal
set "ROOT=%~dp0"
set "VENV_PYTHON=%ROOT%..\.venv\Scripts\python.exe"
set "PYTHONPATH=%ROOT%jarviscli;%PYTHONPATH%"

if exist "%VENV_PYTHON%" (
    "%VENV_PYTHON%" -m jarviscli
) else (
    python -m jarviscli
)

@echo off

set GLOBAL_VERSION=3.13.0
set LOCAL_VERSION=3.11.9
set PYENV_PATH=%USERPROFILE%/.pyenv/pyenv-win

powershell -ExecutionPolicy Bypass -Command "Invoke-WebRequest -UseBasicParsing -Uri 'https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1' -OutFile './install-pyenv-win.ps1'; & './install-pyenv-win.ps1'"

del "install-pyenv-win.ps1"

set PATH=%PYENV_PATH%/bin;%PYENV_PATH%/shims;%PATH%

echo Installing Python %GLOBAL_VERSION%...
call pyenv install %GLOBAL_VERSION%

echo.
echo Setting Python %GLOBAL_VERSION% as the global version...
call pyenv global %GLOBAL_VERSION%

echo.
echo Installing Python %LOCAL_VERSION%...
call pyenv install %LOCAL_VERSION%

echo.
echo Installing ruff for Python %GLOBAL_VERSION%...
call pip install -U ruff

pause

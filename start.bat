@echo off
setlocal enabledelayedexpansion

set GLOBAL_VERSION=3.13.0
set LOCAL_VERSION=3.11.9
set PYENV_PATH=%USERPROFILE%/.pyenv/pyenv-win

powershell -ExecutionPolicy Bypass -Command "Invoke-WebRequest -UseBasicParsing -Uri 'https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1' -OutFile './install-pyenv-win.ps1'; & './install-pyenv-win.ps1'"
if errorlevel 1 (
    echo Failed to install pyenv.
    exit /b 1
)

echo Setting environment variable(s)...
set PATH=%PYENV_PATH%/bin;%PYENV_PATH%/shims;%PATH%

call pyenv --version >nul 2>&1
if errorlevel 1 (
    echo pyenv is not installed or not in PATH.
    exit /b 1
)

echo.
echo Installing Python %GLOBAL_VERSION%...
call pyenv install %GLOBAL_VERSION%
if errorlevel 1 (
    echo Failed to install Python %GLOBAL_VERSION%.
    exit /b 1
)

call pyenv global %GLOBAL_VERSION%
if errorlevel 1 (
    echo Failed to set Python %GLOBAL_VERSION% as the global version.
    exit /b 1
)

echo.
echo Installing Python %LOCAL_VERSION%...
call pyenv install %LOCAL_VERSION%
if errorlevel 1 (
    echo Failed to install Python %LOCAL_VERSION%.
    exit /b 1
)

echo.
echo Installing ruff for Python %GLOBAL_VERSION%...
call pip install -U ruff
if errorlevel 1 (
    echo Failed to install ruff for Python %GLOBAL_VERSION%.
    exit /b 1
)

echo.
echo Updating pip for Python %GLOBAL_VERSION%...
call python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to update pip for Python %GLOBAL_VERSION%.
    exit /b 1
)

call pyenv global %LOCAL_VERSION%
if errorlevel 1 (
    echo Failed to set Python %LOCAL_VERSION% as the global version.
    exit /b 1
)

echo.
echo Updating pip for Python %LOCAL_VERSION%...
call python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to update pip for Python %LOCAL_VERSION%.
    exit /b 1
)

echo.
echo Setting Python %GLOBAL_VERSION% as the global version...
call pyenv global %GLOBAL_VERSION%
if errorlevel 1 (
    echo Failed to revert to Python %GLOBAL_VERSION% as the global version.
    exit /b 1
)

echo.
echo Cleaning up...
del "install-pyenv-win.ps1"


set GIT_URL=https://api.github.com/repos/git-for-windows/git/releases/latest
set RELEASE_JSON=release.json
set INSTALLER=git-installer.exe

echo.
echo Fetching latest git release...
curl -s %GIT_URL% -o %RELEASE_JSON%
if errorlevel 1 (
    echo Failed to fetch release metadata.
    exit /b 1
)

set DOWNLOAD_URL=
for /f "usebackq tokens=*" %%I in (`type %RELEASE_JSON% ^| findstr /i "browser_download_url" ^| findstr "64-bit.exe"`) do (
    set "TEMPORARY=%%I"
)

set "TEMPORARY=%TEMPORARY:browser_download_url=%"
set "TEMPORARY=%TEMPORARY:: =%"
set "TEMPORARY=%TEMPORARY:"=%"

for /f "delims=" %%I in ("%TEMPORARY%") do set "DOWNLOAD_URL=%%I"

echo.
echo Downloading git from %DOWNLOAD_URL%
if "%DOWNLOAD_URL%"=="" (
    echo Failed to parse the git download URL.
    exit /b 1
)

echo.
echo Saving the git installer as %INSTALLER%
curl -L "%DOWNLOAD_URL%" -o %INSTALLER%
if errorlevel 1 (
    echo Failed to download git installer.
    exit /b 1
)

echo.
echo Installing git from %INSTALLER%...
%INSTALLER% /VERYSILENT
if errorlevel 1 (
    echo git installation failed.
    exit /b 1
)

echo.
echo Cleaning up...
del %RELEASE_JSON%
del %INSTALLER%

echo.
echo Cloning the repository into %USERPROFILE%/Documents...
git clone https://github.com/braycarlson/incantation "%USERPROFILE%/Documents/incantation"
if errorlevel 1 (
    echo Failed to clone the repository.
    exit /b 1
)

echo.
echo Installing software...
call python %USERPROFILE%/Documents/incantation/run.py

pause

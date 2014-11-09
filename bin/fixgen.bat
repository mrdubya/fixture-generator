@echo off
rem By default python.exe does not appear in PATH.  Look in various places
rem relative to the script before assuming it is on PATH.
setlocal
rem %~dp0 is the script's directory.
if exist "%~dp0..\python.exe" (
    "%~dp0..\python" "%~dp0fixgen" %*
) else (
    if exist "%~dp0python.exe" (
        "%~dp0python" "%~dp0fixgen" %*
    ) else (
        python "%~dp0fixgen" %*
    )
)
endlocal

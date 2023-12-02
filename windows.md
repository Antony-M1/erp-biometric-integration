To running through script

create a `run_biometric_script.cmd` and past the below code

```
@echo off
 
rem Define your working directory here
set WORKING_DIR="C:\Users\my-user\erp_biometric"
 
rem Find the Python task
for /f "tokens=2" %%i in ('tasklist ^| findstr python.exe') do set PID=%%i
 
rem Kill the Python task if it is running
if defined PID (
    taskkill /F /PID %PID%
    rem Activate the virtual environment
    call %WORKING_DIR%\env\Scripts\activate
 
    rem Run erpnext_sync.py (assumes it's in the working directory)
    python %WORKING_DIR%\erpnext_sync.py
 
    rem Deactivate the virtual environment
    deactivate
) else (
    rem Activate the virtual environment
    call %WORKING_DIR%\env\Scripts\activate
 
    rem Run erpnext_sync.py (assumes it's in the working directory)
    python %WORKING_DIR%\erpnext_sync.py
 
    rem Deactivate the virtual environment
    deactivate
)
 
rem Pause to keep the command window open (you can remove this line if not needed)
pause
```

create a `run_biometric_service_hidden.vbs` and past the below code
```
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "C:\Users\my-user\erp_biometric\run_biometric_service.cmd", 0, False
Set WshShell = Nothing

```

add the file in the `startup` folder in windows


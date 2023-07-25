# erp-biometric-integration

Bio-Metric Issue fixing
Note:- if the command is not working add sudo in front of the command
```
cd
```
```
ls
```
```
cd frappe-bench/biometric-attendance-sync-tool
```
```
nano local_config.py
```
```
rm -rf logs/
```

In this file
Change variable name `IMPORT_START_DATE = {{which_date_you_want}}`
After changing `Ctrl + o`
Enter
`Ctrl + x`
enter

Start the bio metric attendance at the terminal
`python3 erpnext_sync.py` or `python3 push_to_erpnext.py`

Case: if any power or network connection issues happen
```
ps aux | grep python3
```
`erpnext_sync.py` get this file process ID
```
kill -9 <process ID> &   
```
 (for stop the process if not working add sudo at front)


# Kill process
Command
Use
```
ps aux | grep python3
```
To check what are all running in python
```
kill -9 <that_number_run_in_python> &
```
Ex: `kill -9 549 &`

Kill process



Bio-Metric Related Links
* https://github.com/frappe/biometric-attendance-sync-tool
* https://github.com/frappe/biometric-attendance-sync-tool#cli
* https://github.com/frappe/biometric-attendance-sync-tool/releases
* [Integrating ERPNext With Biometric Attendance Devices](https://docs.erpnext.com/docs/v12/user/manual/en/setting-up/articles/integrating-erpnext-with-biometric-attendance-devices)


	



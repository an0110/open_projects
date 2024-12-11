REM cmd -as admin

ipconfig /flushdns
ipconfig /release
ipconfig /renew

netsh winsock reset

netsh int ip reset

shutdown -s -c "bad internet solver - restarting PC in 10-15 seconds" 

pause
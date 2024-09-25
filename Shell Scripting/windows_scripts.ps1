# To run powershell scripts as admin
Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File 'D:\Work\Codes\git repository\Shell Scripting\windows_scripts.ps1'" -Verb RunAs

# To enable(1) and disable User Access Control 
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name EnableLUA -Value 1;

# To enable/disable Window Time Service
Get-Service -Name W32Time | Start-Service
Get-Service -Name W32Time | Stop-Service


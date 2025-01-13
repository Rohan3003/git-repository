# PowerShell script to get the system information

# Get computer system information
Get-WmiObject -Class Win32_ComputerSystem

# Get operating system information
Get-WmiObject -Class Win32_OperatingSystem

# Get processor information
Get-WmiObject -Class Win32_Processor

# Get BIOS information
Get-WmiObject -Class Win32_BIOS



# to disable USB ports 
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\USBSTOR" -Name "Start" -Value 4

# to disable wifi 

# Get the name of Wi-Fi adapter
# Set-ExecutionPolicy RemoteSiged
$wifiAdapter = Get-NetAdapter | Where-Object {$_.Status -eq 'Up' -and $_.NdisPhysicalMedium -eq '802.11'}
Write-Host '$wifiAdapter'

if ($wifiAdapter){
    Disable-NetAdapter -Name $wifiAdapter.Name -Confirm:$false
    Write-Host "Wi-Fi adapter '$(wifiAdapter.Name)' has been disabled."
    }
else{
    Write-Host "No active Wi-Fi adapter found."
}


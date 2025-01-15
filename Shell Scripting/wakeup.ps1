try {
    $com_object = New-Object -ComObject WScript.Shell
    $start_time = Get-Date
    Write-Host "Script started at $start_time"
    Write-Host "Script is running"
    while ($true) {
        $com_object.SendKeys('+{F15}') # Sends the Shift+F15 key combination
        Start-Sleep -Seconds 100 # Sleeps the while loop for 100 seconds
        
    }
} catch {
    Write-Host "Error occured: $_"
    exit 1
} finally {
    Write-Host "Script terminated"
}
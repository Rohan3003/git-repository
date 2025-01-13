# Define countdown time in seconds
$timerDuration = 60 # Example: 60 seconds

# Get the end time
$endTime = (Get-Date).AddSeconds($timerDuration)

# Start the timer
Write-Host "Timer started for $timerDuration seconds."
while ((Get-Date) -lt $endTime) {
    # Calculate the remaining time
    $remainingTime = $endTime - (Get-Date)
    
    # Display the remaining time
    Write-Host ("Remaining time: {0:hh\:mm\:ss}" -f $remainingTime) -NoNewline
    Start-Sleep -Seconds 1
    Write-Host "`r" -NoNewline
}

# Timer ends
Write-Host "Time's up!" -ForegroundColor Green
[System.Media.SystemSounds]::Exclamation.Play() # Play a notification sound

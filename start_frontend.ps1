# PowerShell script to start the frontend development server

Write-Host "Changing directory to flux-frontend..."
Set-Location -Path .\flux-frontend

Write-Host "Starting frontend development server (yarn dev)..."
Write-Host "If this command fails, ensure 'yarn' is installed and in your PATH,"
Write-Host "and run 'yarn install' in the flux-frontend directory first."
Write-Host ""

# Start yarn dev in the current window.
# Use Start-Process if you want it in a new window, but -NoExit might not work as expected there.
yarn dev

# Keep the PowerShell window open after the script finishes (if run directly without -NoExit)
# If running like "powershell .\start_frontend.ps1", it might close.
# Running "powershell -NoExit -File .\start_frontend.ps1" is more reliable for keeping it open.
Read-Host -Prompt "Press Enter to exit" 
# PowerShell script to start the backend server in the 'ideal' conda environment

Write-Host "Starting Backend Server..."

Write-Host "Attempting to run Python backend in 'ideal' conda environment using 'conda run'..."
Write-Host "If this fails, ensure 'conda' is in your PATH, the 'ideal' environment exists,"
Write-Host "and necessary packages (like python) are installed in 'ideal'."
Write-Host "Check flux-backend\requirements.txt."
Write-Host ""

# Execute conda run to start the python app within the specified environment.
# The python script path is relative to where this powershell script is located.
cd D:\Code2025\Flux_ideal_local\flux-panel\flux-backend

conda run -n ideal --no-capture-output --live-stream python .\flux-backend\app.py --env=dev




# The Read-Host might not be reached if the python server runs indefinitely.
# It's here mainly for cases where the command might fail quickly.
Write-Host "Backend process should be running. Press Ctrl+C in the console to stop the server."
Read-Host -Prompt "Press Enter to exit this script window (if the server has stopped)" 
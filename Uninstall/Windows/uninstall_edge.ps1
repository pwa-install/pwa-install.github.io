# Echo message
Write-Output "Uninstalling Microsoft Edge"

# Check if running as administrator
if (!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Error "You need to run this script as an administrator."
    exit
}

# Edge Uninstallation Path (using the uninstaller directly)
$EdgePath = "$env:ProgramFiles (x86)\Microsoft\Edge\Application\msedge.exe"
if (Test-Path $EdgePath) {
    Start-Process -FilePath $EdgePath -ArgumentList "--uninstall --system-level --force-uninstall" -Verb RunAs
    Write-Output "Microsoft Edge has been successfully uninstalled."
} else {
    Write-Output "Microsoft Edge not found."
}
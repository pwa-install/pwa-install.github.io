# Echo message
Write-Output "Uninstalling Google Chrome"

# Check if running as administrator
if (!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Error "You need to run this script as an administrator."
    exit
}

# Get Google Chrome installation
$app = Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name = 'Google Chrome'"

# Uninstall Google Chrome
if ($app -ne $null) {
    $app.Uninstall()
    Write-Output "Google Chrome has been successfully uninstalled."
} else {
    Write-Output "Google Chrome not found."
}
#!/bin/bash

# Echo message
echo "Uninstalling Google Chrome"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "You need to run this script as root." 
   exit 1
fi

# Define Google Chrome application path
CHROME_APP_PATH="/Applications/Google Chrome.app"

# Uninstall Google Chrome
if [ -d "$CHROME_APP_PATH" ]; then
    rm -rf "$CHROME_APP_PATH"
    echo "Google Chrome has been successfully uninstalled."
else
    echo "Google Chrome not found."
fi
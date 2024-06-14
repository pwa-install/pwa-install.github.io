#!/bin/bash

# Echo message
echo "Uninstalling Google Chrome"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "You need to run this script as root." 
   exit 1
fi

# Uninstall Google Chrome
if command -v google-chrome >/dev/null 2>&1; then
    apt-get remove --purge google-chrome-stable -y
    echo "Google Chrome has been successfully uninstalled."
else
    echo "Google Chrome not found."
fi
#!/bin/bash

# Echo message
echo "Uninstalling Microsoft Edge"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "You need to run this script as root." 
   exit 1
fi

# Uninstall Microsoft Edge
if command -v microsoft-edge >/dev/null 2>&1; then
    apt-get remove --purge microsoft-edge-stable -y
    echo "Microsoft Edge has been successfully uninstalled."
else
    echo "Microsoft Edge not found."
fi
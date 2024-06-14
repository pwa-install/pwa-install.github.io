#!/bin/bash

# Echo message
echo "Uninstalling Microsoft Edge"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "You need to run this script as root." 
   exit 1
fi

# Define Microsoft Edge application path
EDGE_APP_PATH="/Applications/Microsoft Edge.app"

# Uninstall Microsoft Edge
if [ -d "$EDGE_APP_PATH" ]; then
    rm -rf "$EDGE_APP_PATH"
    echo "Microsoft Edge has been successfully uninstalled."
else
    echo "Microsoft Edge not found."
fi
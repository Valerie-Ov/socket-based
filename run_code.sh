#!/bin/bash

# Ensure traceroute is installed
if ! command -v traceroute &> /dev/null; then
    echo "[INFO] 'traceroute' not found. Installing..."
    sudo apt-get update
    sudo apt-get install -y traceroute
fi

python3 server.py &
SERVER_PID=$!
sleep 1  # Give server time to start and write .env

# Simulate client input
echo -e "https://github.com\nexit" | python3 client.py

# Kill the server
kill $SERVER_PID

#!/bin/bash
# Ares Pulse: Syncs local firewall with the Global Hub

ARES_HUB_URL="http://your-hub-ip:8888/v1/global_blacklist"

# 1. Fetch the latest high-level threats
THREATS=$(curl -s $ARES_HUB_URL | jq -r '.ips[]')

# 2. Feed them to the Void (the Go script we wrote)
for ip in $THREATS; do
    echo "ARES PULSE: Syncing global threat $ip to local Void."
    ./void $ip
done

#!/bin/bash
# Ares Nexus: The Command Center

echo "1. Generate New Agent"
echo "2. View The Void (Current Blackholes)"
echo "3. Review Evidence"
read -p "Selection: " choice

case $choice in
  1)
    read -p "Site Name: " name
    read -p "Log Path: " path
    python3 -c "from agents.generator import bake_ai_agent; bake_ai_agent('$name', '$path')"
    ;;
  2)
    ip route show type blackhole
    ;;
esac

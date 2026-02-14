#!/bin/bash
# Ares Capture: Logs the last 100 packets from an attacker before the Void
IP=$1
LOG_FILE="evidence/attack_${IP}_$(date +%s).pcap"

echo "ARES: Capturing evidence for target $IP..."
# Captures traffic specifically from the attacker's IP
sudo tcpdump -i eth0 src $IP -c 100 -w $LOG_FILE &

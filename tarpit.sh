#!/bin/bash
# The Dreadnought: Sends 1 byte of junk every 10 seconds to a specific port
while true; do 
  echo -n "0" | nc -l -p 8080 -q 10; 
  sleep 10; 
done

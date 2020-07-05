#!/bin/bash
nmap -v -sn -n $1 -oG - | grep "Status: Up" | awk '{print $2, "is ocupied"}' | xargs -n3 echo ip
#!/bin/bash
nmap -v -sn -n $1 -oG - | awk '/Status: Up/{printf "ip %s is ocupied\n", $2}'
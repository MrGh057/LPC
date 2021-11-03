#! /bin/bash

sudo nmap -sS --min-rate 5000 -vvv -n -Pn 189.207.27.21 -oG nmap.txt

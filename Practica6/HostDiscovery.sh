#!/bin/bash

for i in $(seq 2 254); do
    timeout 1 bash -c "ping -c 1 189.207.27.$i > /dev/null 2>&1" && echo "Host 189.207.27.$i --> ACTIVO"
done

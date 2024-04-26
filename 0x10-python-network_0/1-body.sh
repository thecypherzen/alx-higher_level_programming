#!/bin/bash
# sends a get request to a server
res="$(curl -Is $1 |head -1|cut -d ' ' -f2)"
if [[ "$res" -eq 200 ]]; then
    curl -s "$1";
fi

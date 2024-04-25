#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the
# +size of the body of the response in bytes using curl

if (( "$#" > 0 )); then
    res="$(curl -Is "$1" | grep Content-Length | tr -d ' ' | cut -d : -f2)"
    echo "$res"
fi

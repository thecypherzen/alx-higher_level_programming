#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the
echo "$(curl -Is "$1" | grep Content-Length | tr -d ' ' | cut -d : -f2)"

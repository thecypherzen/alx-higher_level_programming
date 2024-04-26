#!/bin/bash
# lists http requests a server can handle
curl -sLI "$1" | grep -iw "allow" | cut -d ' ' -f 2-

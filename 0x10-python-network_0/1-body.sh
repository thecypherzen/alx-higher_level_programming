#!/bin/bash
# sends a get request to a server
echo -n "$(curl -sf $1 -m 10)"

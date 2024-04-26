#!/bin/bash
# displays status code of a request response
curl -s -o /dev/null -w "%{http_code}" "$1"

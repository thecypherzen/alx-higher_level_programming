#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays the
   value of the variable 'X-Request-Id' in the response header
   => must use the packages 'requests' and 'sys'
   => must not import packages other than 'requests' and 'sys'
   => no need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url).__dict__
    headers = response.get("headers", None)
    res = headers.get("X-Request-Id", None)
    print(res)

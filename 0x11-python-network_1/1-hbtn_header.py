#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays the
   value of the X-Request-Id variable found in the header of the response.
   => must use the packages urllib and sys
   => must not import packages other than urllib and sys
   => must use with context manager
   => no need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    from urllib.request import urlopen
    import sys

    if len(sys.argv) > 1:
        url = sys.argv[1]
        with urlopen(url) as response:
            headers = response.headers._headers
        value = [tup for tup in headers if tup[0] == "X-Request-Id"]
        print(value[0][1])

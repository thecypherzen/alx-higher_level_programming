#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays the
   body of the response (decoded in utf-8).

   => have to manage urllib.error.HTTPError exceptions and print:
      Error code: followed by the HTTP status code
   => must use the packages urllib and sys and can only import them
   => must use with context manager
   => no need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]

    # try to make request
    try:
        with urlopen(url) as response:
            msg = response.read()
            print(str(msg, encoding="utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")

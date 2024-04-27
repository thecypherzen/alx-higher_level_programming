#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays the
   body of the response.

   => If the HTTP status code is greater than or equal to 400, print:
      Error code: followed by the HTTP status code
   => must use the packages 'urllib' and 'sys' and can only import them
   => no need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    status_code = response.status_code
    if status_code >= 400:
        print("Error code:", status_code)
    else:
        print(response.text)

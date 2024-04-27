#!/usr/bin/python3
"""A script that takes in a URL and an email, sends a POST request to the
   passed URL with the email as a parameter, and displays the body of the
   response (decoded in utf-8).
   => the email must be sent in the email variable
   => must use the packages urllib and sys and can only import them
   => must use with context manager
   => no need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys

    # create request
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    data = urlencode(data)
    data = data.encode("utf-8")
    request = Request(url, data)

    # make request and extract info
    with urlopen(request) as response:
        message = response.read()
    print(str(message, encoding="ascii"))

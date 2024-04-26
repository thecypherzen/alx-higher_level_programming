#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status
   => must use the package urllib
   => can only import urllib
   => The body of the response must be displayed like so:
      Body Response:
          - type: <class 'bytes'>$
          - content: b'OK'$
          - utf8 content: OK$
"""
if __name__ == "__main__":
    from urllib.request import urlopen

    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        content = response.read()
        msg = f"Body response\n\t- type: {type(content)}" +\
            f"\n\t- content: {content}" + \
            f"\n\t- utf8 content: {str(content, encoding='utf-8')}"
    print(msg)

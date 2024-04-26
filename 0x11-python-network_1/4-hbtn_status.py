#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status

   => must use the package requests and should only import it
   => the body of the request must be in the order:
      Body response:
          - type: <class 'str'>
          - content: OK
"""
if __name__ == "__main__":
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status").__dict__
    message = str(response.get("_content", None), encoding="ascii")
    result = (f"Body response:\n\t- type: {type(message)}\n" +
              f"\t- content: {message}")
    print(result)

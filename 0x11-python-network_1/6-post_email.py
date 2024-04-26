#!/usr/bin/python3
"""A script that takes in a URL and an email, sends a POST request to the
   passed URL with the email as a parameter, and displays the body of the
   response.
   => the email must be sent in the email variable
   => must use the packages 'requests' and 'sys' and can only import them
   => no need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    import requests
    import sys

    # create request
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]}).__dict__
    message = response.get('_content', None)
    print(str(message, encoding='ascii'))

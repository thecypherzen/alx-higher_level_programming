#!/usr/bin/python3
"""A script that takes takes in a GitHub username and password uses the
   GitHub API to display its id

   => must use 'Basic Authentication' with a 'personal access token'
      as password to access to your information (only read:user permission
      is needed)
   => the first arg will be the 'username' and the second will be
      the 'password'
   => if the response body is properly JSON formatted and not empty, display
   => must use the packages 'requests' and 'sys' and only alled to import them
   => don’t need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    import requests
    import sys

    _user = sys.argv[1]
    _token = sys.argv[2]
    url = f"https://api.github.com/user"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, headers=headers)

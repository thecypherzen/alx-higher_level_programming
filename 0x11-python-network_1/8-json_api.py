#!/usr/bin/python3
"""A script that takes takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.

   => the letter must be sent in the variable q
   => if no argument is given, set q=""
   => if the response body is properly JSON formatted and not empty, display
      the id and name like this: [<id>] <name>, otherwise:
      => display 'Not a valid JSON' if the JSON is invalid
      => display 'No result' if the JSON is empty
   => must use the packages 'requests' and 'sys' and only alled to import them
"""
if __name__ == "__main__":
    import requests
    from requests.exceptions import JSONDecodeError as jsonError
    import sys

    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    data = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)
    try:
        json_res = response.json()
        if not json_res:
            print("No result")
        else:
            print(f"[{json_res.get('id')}] {json_res.get('name')}")
    except jsonError:
        print("Not a valid JSON")

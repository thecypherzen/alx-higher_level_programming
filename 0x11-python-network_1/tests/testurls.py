#!/usr/bin/python3
'''
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = "https://www.google.com"
q = {'q': "things fall apart"}
url = url + '?' + urlencode(q)

response = urlopen(url)
content = response.read()
with open("searchresults.html", 'w') as f:
    f.write(str(content))
'''

# Working with requests
import requests

url = "http://www.ridgesolid.tech"
res = requests.get(url)

mtest = "testutil"
print(bytes(mtest, encoding='utf-8'))

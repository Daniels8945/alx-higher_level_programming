#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""

import urllib.request


url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    
with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))

#!/usr/bin/python3
import urllib.request
"""Fetches https://alx-intranet.hbtn.io/status."""


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))

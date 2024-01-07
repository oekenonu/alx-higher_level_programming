#!/usr/bin/python3
""" Module to take URL and display body of response
    but catch errors using requests module"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)

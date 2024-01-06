#!/usr/bin/python3
""" Module to post an email using urllib """

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    value = dict(email=sys.argv[2])
    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

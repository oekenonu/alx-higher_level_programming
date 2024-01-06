#!/usr/bin/python3
""" Module to read value of X-Request-Id from header """

if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))

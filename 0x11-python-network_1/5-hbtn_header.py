#!/usr/bin/python3
""" Module to read value of X-Request-Id from header """

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))

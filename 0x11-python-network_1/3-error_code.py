#!/usr/bin/python3
""" Module to use urllib.error.HTTPError class """

if __name__ == '__main__':
    import sys
    import urllib.request
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode(encoding='utf-8'))
    except HTTPError as e:
        print('Error code:', e.status)

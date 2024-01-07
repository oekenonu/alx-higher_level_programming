#!/usr/bin/python3
""" Module to post an email using requests """

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    value = dict(email=sys.argv[2])
    r = requests.post(url, value)
    print('Your email is :', r.text)

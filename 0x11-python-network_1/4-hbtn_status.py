#!/usr/bin/python3
# Script using requests to show url status

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print(f'\t- type: {type(r.text)}')
    print(f'\t- content: {(r.text)}')

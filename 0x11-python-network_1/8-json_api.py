#!/usr/bin/python3
""" Module to take a letter and post using requests """

if __name__ == '__main__':
    import requests
    import sys

    base_url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        arg = ''
    else:
        arg = sys.argv[1]
    data = dict(q=arg)
    try:
        r = requests.post(base_url, data=data)
        response = r.json()
        if response == {}:
            print('No result')
        else:
            print(f'[{response.get("id")}] response.get("name")}')
    except ValueError as e:
        print('Not a valid JSON')

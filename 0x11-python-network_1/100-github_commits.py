#!/usr/bin/python3
""" Module to list 10 most recent commits from GitHub repository. """


if __name__ == '__main__':
    import sys
    import requests
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(0, 10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

#!/usr/bin/python3
"""subs module"""


import requests


def number_of_subscribers(subreddit):
    """to count numb of subscriber"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except ValueError:
        return 0

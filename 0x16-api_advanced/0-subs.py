#!/usr/bin/python3
"""subs module"""


from requests import get


def number_of_subscribers(subreddit):
    """to count numb of subscriber"""
    url = url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    try:
        js = response.json()
    except ValueError:
        return 0
    data = js.get("data")
    if data:
        sub_count = data.get("subscribers")
        if sub_count:
            return sub_count

    return 0

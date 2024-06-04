#!/usr/bin/python3
"""
0-sub
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscriber for a given subreddit.
    if the subreddit is invalid, return 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]

    return 0

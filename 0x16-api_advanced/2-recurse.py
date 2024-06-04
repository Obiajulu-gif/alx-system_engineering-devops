#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of hot article titles for a given subreddit.
    If no results are found, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My Reddit API Client"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post["data"]["title"]
                        for post in data["data"]["children"]])
    return hot_list

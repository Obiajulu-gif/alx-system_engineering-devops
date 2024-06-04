#!/usr/bin/python3
"""
100-count
"""
import requests
import re

MAX_DEPTH = 10


def count_words(
        subreddit,
        word_list,
        hot_list=None,
        after=None,
        word_count={},
        depth=0):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if hot_list is None:
        hot_list = []
    if word_count == {}:
        word_count = {word.lower(): 0 for word in word_list}

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

        for title in hot_list:
            for word in word_list:
                word_lower = word.lower()
                count = len(
                    re.findall(
                        r'\b' +
                        re.escape(word_lower) +
                        r'\b',
                        title.lower()))
                word_count[word_lower] += count

        if data["data"]["after"]:
            if depth < MAX_DEPTH:
                count_words(
                    subreddit,
                    word_list,
                    hot_list,
                    data["data"]["after"],
                    word_count,
                    depth + 1)
        else:
            sorted_word_count = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        return

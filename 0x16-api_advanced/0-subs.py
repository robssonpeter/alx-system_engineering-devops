#!/usr/bin/python3
""" Script to fetch subscribers """

import requests

def number_of_subscribers(subreddit):
    """ Set a custom User-Agent to avoid Too Many Requests error """
    headers = {'User-Agent': 'Custom User-Agent'}

    """ Make the API request to get subreddit information """
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json", headers=headers)

    """ Check if the request was successful """
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            return 0
    elif response.status_code == 404:
        return 0
    else:
        return 0  
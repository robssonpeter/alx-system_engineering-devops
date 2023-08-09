#!/usr/bin/python3
""" The script to get top ten subreddits """
import requests

def top_ten(subreddit):
    """ Set a custom User-Agent to avoid Too Many Requests error """
    headers = {'User-Agent': 'Custom User-Agent'}

    """ Make the API request to get the hot posts in the subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers)

    """ Check if the request was successful """
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            for i, post in enumerate(posts[:10], start=1):
                title = post['data']['title']
                print(f"{i}. {title}")
        except KeyError:
            print("None")
    else:
        print("None")


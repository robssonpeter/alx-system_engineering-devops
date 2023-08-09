""" Hot topics with recursion """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Set a custom User-Agent to avoid Too Many Requests error """
    headers = {'User-Agent': 'Alx-Student'}

    """ Prepare parameters for the API request """
    params = {'limit': 100, 'after': after}

    """ Make the API request to get the hot posts in the subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params)

    """ Check if the request was successful """
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            hot_list.extend([post['data']['title'] for post in posts])

            """ Check for pagination """
            after = data['data']['after']
            if after:
                """ Recursively call the function with the after parameter """
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except KeyError:
            return None
    else:
        return None

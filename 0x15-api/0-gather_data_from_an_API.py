#!/usr/bin/python3
""" Script to make a request to an API """

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    """ Run only if this is the main module """
    with requests.get(users_url) as usr_resp:
        name = usr_resp.json()['name']
        is_done = "is done with tasks"
        with requests.get(url) as resp:
            completed = []
            total = 0
            user_id = argv[1]

            for todo in resp.json():
                if todo['userId'] == int(user_id):
                    total += 1
                    if todo['completed'] is True:
                        completed.append(todo)
            if len(completed) > 0:
                text = f"Employee {name} {is_done}({len(completed)}/{total}):"
                print(text)
                for task in completed:
                    print("\t"+task['title'])

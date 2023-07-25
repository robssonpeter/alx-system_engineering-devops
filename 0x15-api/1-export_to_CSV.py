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
        username = usr_resp.json()['username']
        is_done = "is done with tasks"
        with requests.get(url) as resp:
            completed = []
            all_tasks = []
            total = 0
            user_id = argv[1]

            for todo in resp.json():
                if todo['userId'] == int(user_id):
                    total += 1
                    all_tasks.append(todo)
                    if todo['completed'] is True:
                        completed.append(todo)
            csv_content = ""
            if len(completed) > 0:
                for task in all_tasks:
                    is_complete = task['completed']
                    csv_content += f"\"{user_id}\",\"{username}\","
                    csv_content += f"\"{is_complete}\",\"{task['title']}\"\n"
            with open(f"{user_id}.csv", "+w", encoding="UTF-8") as fp:
                fp.write(csv_content)

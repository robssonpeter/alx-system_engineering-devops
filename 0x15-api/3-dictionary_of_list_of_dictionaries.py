#!/usr/bin/python3
""" Script to make a request to an API """

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = f"https://jsonplaceholder.typicode.com/users"

    """ Run only if this is the main module """
    with requests.get(users_url) as usr_resp:
    
        all_data = {

        }
        all_names = {}
        for data in usr_resp.json():
            all_data[data['id']] = []
            all_names[data['id']] = {"username": data['username']}

        with requests.get(url) as resp:
            completed = []
            total = 0
            for todo in resp.json():
                todo_row = {
                    "username": all_names[todo['userId']],
                    "task": todo['title'],
                    "completed": todo['completed'],
                }
                all_data[todo['userId']].append(todo_row)
        with open("todo_all_employees.json", "w") as fp:
            fp.write(json.dumps(all_data))

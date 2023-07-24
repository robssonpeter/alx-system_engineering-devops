#!/usr/bin/python3
"""
Script to make a request to an API
"""

import requests
from sys import argv

try:
    protocal = "https://"
    domain = "my-json-server.typicode.com"
    uri = f"/robssonpeter/alx-system_engineering-devops/employees/{argv[1]}"
    url = protocal+domain+uri
    with requests.get(url) as req:
        result = req.json()
        if len(result) > 0:
            length = result['total']
            is_done = "is done with tasks"
            tasks = result['tasks']
            text = f"{result['name']} {is_done}({len(tasks)}/{length}):"
            print(text)
            for task in req.json()['tasks']:
                print("\t"+task)
except IndexError:
    print('there is an error')

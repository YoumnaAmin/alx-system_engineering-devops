#!/usr/bin/python3
"""Script to gather data from an API"""

import csv
import requests
import sys


if len(sys.argv) < 2:
    print("Usage: ./script.py <user_id>")
    sys.exit(1)


user_id = sys.argv[1]


user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'


user_response = requests.get(user_url)
todos_response = requests.get(todos_url)


if user_response.status_code == 200:
    user_data = user_response.json()
    username = user_data["username"]
else:
    sys.exit(1)


if todos_response.status_code == 200:
    todos_data = todos_response.json()
    tasks = []
    for task in todos_data:
        tasks.append([
            user_id,
            username,
            task['completed'],
            task['title']
        ])
    csv_file = f"{user_id}.csv"
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)
else:
    sys.exit(1)

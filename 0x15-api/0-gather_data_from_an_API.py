#!/usr/bin/python3
"""Script to gather data from an API"""

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
    name = user_data["name"]
else:
    print(f"Error: Unable to fetch user data (status code: \
          {user_response.status_code})")
    sys.exit(1)


if todos_response.status_code == 200:
    todos_data = todos_response.json()
    completed_tasks = [task for task in todos_data if task['completed']]
    completed = len(completed_tasks)
    total_tasks = len(todos_data)

    print(f"Employee {name} is done with tasks({completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
else:
    print(f"Error: Unable to fetch todos data (status code: \
          {todos_response.status_code})")
    sys.exit(1)

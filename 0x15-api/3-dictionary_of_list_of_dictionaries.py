#!/usr/bin/python3
"""Script to gather data from an API and export to JSON"""

import json
import requests
import sys


users_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'


users_response = requests.get(users_url)
todos_response = requests.get(todos_url)

if users_response.status_code == 200:
    users_data = users_response.json()
    all_tasks = {}
    for user in users_data:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = [task for task in todos_response.json() if task['userId'] == user['id']]
        tasks_data = []
        for task in user_tasks:
            tasks_data.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
        all_tasks[user_id] = tasks_data
    json_file_name = 'todo_all_employees.json'
    with open(json_file_name, mode='w') as json_file:
        json.dump(all_tasks, json_file)
else:
    sys.exit(1)

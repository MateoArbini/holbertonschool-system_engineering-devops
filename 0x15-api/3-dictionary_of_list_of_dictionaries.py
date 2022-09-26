#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python script to export data
in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [
{"username": "USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
'''

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        filename = "todo_all_employees.json"
        users = requests.get('https://jsonplaceholder.typicode.com/users')
        users = users.json()
        x = requests.get('https://jsonplaceholder.typicode.com/todos')
        x = x.json()
        dictionary = {}
        final_dict = {}
        list_of_dicts = []

        for user in users:
            new_list = []
            for task in x:
                dictionary['username'] = user['username']
                dictionary['task'] = task['title']
                dictionary['completed'] = task['completed']
                list_of_dicts.append(dictionary)
            final_dict[user['id']] = list_of_dicts

        with open(filename, 'w') as f:
            f.write(json.dumps(final_dict))
        f.close()
    except Exception as e:
        print(e)

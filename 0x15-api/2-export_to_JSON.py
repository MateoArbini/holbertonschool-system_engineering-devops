#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python script to export data in
the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

File name must be: USER_ID.json
'''

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        eID = argv[1]
        filename = "{}.json".format(eID)
        users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(eID))
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(eID))
        users = users.json()
        tasks = tasks.json()
        list_of_dicts = []
        final_dict = {}

        for field in tasks:
            dictionary = {}
            dictionary["task"] = field['title']
            dictionary["completed"] = field['completed']
            dictionary["username"] = users.get('username')
            list_of_dicts.append(dictionary)

        final_dict[users.get('id')] = list_of_dicts

        with open(filename, 'w') as f:
            f.write(json.dumps(final_dict))
        f.close()
    except Exception as e:
        print(e)
            

#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python script to export
data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
'''

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        eID = argv[1]
        # Users is a DICTIONARY
        users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(eID))
        users = users.json()
        # Tasks is a LIST
        x = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(eID))
        x = x.json()

        with open('USER_ID.csv', 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for field in x:
                row = [users.get('id'), users.get('username'),
                       field['completed'], field['title']]
                writer.writerow(row)
        f.close()
    except Exception as e:
        print(e)

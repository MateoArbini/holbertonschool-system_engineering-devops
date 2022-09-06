#!/usr/bin/python3
'''
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Requirements:

- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list
- progress in this exact format:
    - First line: Employee EMPLOYEE_NAME is done with tasks
      (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    - EMPLOYEE_NAME: name of the employee
    - NUMBER_OF_DONE_TASKS: number of completed tasks
    - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
      completed and non-completed tasks
    - Second and N next lines display the title of complete
      tasks: TASK_TITLE (1 tabulation and 1 space before the TASK_TITLE)
'''

import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        TOTAL_NUMBER_OF_TASKS = 0
        NUMBER_OF_DONE_TASKS = 0
        eID = argv[1]
        users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(eID))
        users = users.json()
        x = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(eID))
        x = x.json()

        # Here I get the total tasks and the total completed
        for field in tasks:
            TOTAL_NUMBER_OF_TASKS += 1
            if field['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1

        # Here I get the employee name and the task name
        EMPLOYEE_NAME = users['name']

        print('Employee {} is done with tasks({}/{}):'
              .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))
        for field in tasks:
            if field['title'] and field['completed'] is True:
                print("\t  {}".format(field['title']))

    except Exeptions:
        print(Exceptions)

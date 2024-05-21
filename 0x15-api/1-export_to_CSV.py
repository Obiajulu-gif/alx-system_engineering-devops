#!/usr/bin/python3
"""
Script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Failed to retrieve data for employee {}".format(employee_id))

    params = {"userId": employee_id}

    todo_url = "{}/todos".format(url)

    todo_response = requests.get(todo_url, params=params)

    user = user_response.json()
    todos = todo_response.json()

    TASK_TITLE = [todo.get("title")
                  for todo in todos
                  if todo.get("completed") is True]
    NUMBER_OF_DONE_TASKS = len(todos)
    TOTAL_NUMBER_OF_TASKS = len(TASK_TITLE)
    EMPLOYEE_NAME = user.get("name")

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME,
                  TOTAL_NUMBER_OF_TASKS,
                  NUMBER_OF_DONE_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))

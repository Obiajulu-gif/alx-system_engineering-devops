#!/usr/bin/python3
"""
Script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
and exports it to a JSON file.
"""

import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_url = "{}/users/{}".format(url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Failed to retrieve data for employee {}".format(employee_id))
        sys.exit(1)

    # Fetch todos data
    params = {"userId": employee_id}
    todo_url = "{}/todos".format(url)
    todo_response = requests.get(todo_url, params=params)

    user = user_response.json()
    todos = todo_response.json()

    # Extract relevant data
    EMPLOYEE_NAME = user.get("username")  # Fetch username instead of name
    USER_ID = user.get("id")
    TASKS = [{"task": todo.get("title"),
              "completed": todo.get("completed"),
              "username": EMPLOYEE_NAME} for todo in todos]

    # Print task progress
    completed_tasks = [task["task"] for task in TASKS if task["completed"]]
    total_tasks = len(TASKS)
    completed_count = len(completed_tasks)

    for task in completed_tasks:
        print("\t {}".format(task))

    # Export JSON
    json_data = {str(USER_ID): TASKS}
    json_filename = "{}.json".format(USER_ID)
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

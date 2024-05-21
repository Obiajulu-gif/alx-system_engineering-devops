#!/usr/bin/python3
"""
Script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
and exports it to a CSV file.
"""

import requests
import sys
import csv

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
    EMPLOYEE_NAME = user.get("name")
    USER_ID = user.get("id")
    TASKS = [{"username": EMPLOYEE_NAME,
              "task": todo.get("title"),
              "completed": todo.get("completed")} for todo in todos]

    completed_tasks = [task["task"] for task in TASKS if task["completed"]]
    total_tasks = len(TASKS)
    completed_count = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          completed_count,
                                                          total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))
    # Export CSV
    csv_filename = "{}.csv".format(USER_ID)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in TASKS:
            writer.writerow([USER_ID, task["username"],
                            task["completed"], task["task"]])

    print(f"Data exported to {csv_filename}")

#!/usr/bin/python3
"""
Script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Failed to retrieve data for employee {}".format(employee_id))
        return
    params = {"userId": employee_id}

    todo_url = "{}/todos".format(url)

    todo_response = requests.get(todo_url, params=params)

    user = user_response.json()
    todos = todo_response.json()

    complete = [todo.get("title")
                for todo in todos
                if todo.get("completed") is True]
    total_task = len(todos)
    complete_task = len(complete)

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          complete_task,
                                                          total_task))
    for task in complete:
        print("\t {}".format(task))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")

    employee_id = int(sys.argv[1])

    get_employee_todo_progress(employee_id)

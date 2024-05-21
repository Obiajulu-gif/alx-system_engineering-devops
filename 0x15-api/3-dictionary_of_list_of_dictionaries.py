#!/usr/bin/python3
"""
Script that, using this REST API,
returns information about all employees' TODO list progress
and exports data in the JSON format.
"""

import requests
import json

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get(f"{url}/users")
    users = users_response.json()

    # Dictionary to store all user data
    all_user_data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # Get the user's TODO list
        todos_response = requests.get(
            f"{url}/todos", params={"userId": user_id})
        todos = todos_response.json()

        # List to store tasks for this user
        user_tasks = []

        for todo in todos:
            task_data = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            user_tasks.append(task_data)

        # Add user's tasks to the dictionary
        all_user_data[user_id] = user_tasks

    # Export data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_user_data, json_file)

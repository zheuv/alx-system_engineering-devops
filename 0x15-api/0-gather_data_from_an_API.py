#!/usr/bin/python3


import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Fetch employee details
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch employee's todos
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate the number of completed and total tasks
        total_tasks = len(todos_data)
        done_tasks = [todo['title'] for todo in todos_data if todo['completed']]
        number_of_done_tasks = len(done_tasks)

        # Display the results
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID.")

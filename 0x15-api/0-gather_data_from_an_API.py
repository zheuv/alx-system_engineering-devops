#!/usr/bin/python3
""" Module """
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    This function retrieves the employee's name and their TO
    It then calculates the number of completed tasks and the total
    Additionally, it lists the titles of the completed tasks.
    Args:
        employee_id (int): The ID of the employee whose TODO list
    Raises:
        requests.exceptions.RequestException: If there
    """
    try:
        # Fetch employee details
        user = 'https://jsonplaceholder.typicode.com/users/'
        user_response = requests.get(f'{user}{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch employee's todos
        todo = 'https://jsonplaceholder.typicode.com/todos?userId='
        todos_response = requests.get(f'{todo}{employee_id}')
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate the number of completed and total tasks
        tt = len(todos_data)
        done_tasks = []
        for td in todos_data:
            if td['completed']:
                dons_tasks.append(td)
        ndt = len(done_tasks)

        # Display the results
        print(f"Employee {employee_name} is done with tasks({ndt}/{tt}):")
        for task in done_tasks:
            print(f"\t {task}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    """
    Main entry point of the script.
    This block checks if the correct number of
    and calls the get_employee_todo_progress function.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID.")

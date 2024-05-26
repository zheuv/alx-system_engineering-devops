#!/usr/bin/python3
""" module doc """
import json
import requests


def main():
    id = 1
    data_dict = {}

    while True:
        url = "https://jsonplaceholder.typicode.com/"
        users = f"users?id={id}"
        todos = f"todos?userId={id}"
        userData = requests.get(f"{url}{users}").json()

        if not userData:
            break

        userName = userData[0].get("username")
        todosData = requests.get(f"{url}{todos}").json()

        data_dict[id] = [
            {
                "username": userName,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todosData
        ]

        id += 1

    with open("todo_all_employees.json", "w") as f:
        json.dump(data_dict, f)


if __name__ == "__main__":
    main()

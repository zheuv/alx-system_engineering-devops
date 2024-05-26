#!/usr/bin/python3
""" module doc """
import requests
import sys


def main():
    """ def com """
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done = f'{todos}&completed=true'
    notDone = f'{todos}&completed=false'
    userData = requests.get(f'{url}{users}').json()
    Name = userData[0].get("name")
    userName = userData[0].get("username")
    todosData = requests.get(f'{url}{todos}').json()
    todosDone = requests.get(f'{url}{done}').json()
    doneN = len(todosDone)
    totalN = len(todosData)
    """Export into csv"""
    with open(f'{id}.csv', 'w') as f:
        for todo in todosData:
            data = f'"{id}","{userName}","{todo.get("completed")}",'
            data2 = f'"{todo.get("title")}"\n'
            f.write(data+data2)


if __name__ == "__main__":
    main()

"""
Goal: Write a simple command-line program to manage tasks that:
1. Can add a new task.
2. Can delete an existing task.
3. Saves the task list to a `tasks.json` file when exiting.
4. Loads the previous list from the file when restarted.
"""

import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu():
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit and save")

tasks = load_tasks()
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "2":
        new_task = input("New task: ")
        tasks.append(new_task)
    elif choice == "3":
        idx = int(input("Task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
    elif choice == "4":
        save_tasks(tasks)
        print("Saved. Goodbye!")
        break
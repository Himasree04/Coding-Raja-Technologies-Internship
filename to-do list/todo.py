import json
import os
from datetime import datetime

# Define the file where tasks will be stored
TASKS_FILE = 'tasks.json'

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (high, medium, low): ").lower()
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    task = {
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    list_tasks(tasks)
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def complete_task(tasks):
    list_tasks(tasks)
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Function to list tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{i}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']} | Status: {status}")

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Complete Task")
    print("4. List Tasks")
    print("5. Exit")

# Main function
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import json
import os

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    # Convert task to dictionary for saving to JSON
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed
        }

def save_tasks(tasks):
    """Saves the list of Task objects to a JSON file."""
    with open('tasks.json', 'w') as f:
        # Convert list of objects to list of dicts
        json.dump([task.to_dict() for task in tasks], f, indent=4)
    print("Data saved successfully.")

def load_tasks():
    """Loads tasks from the JSON file and returns a list of Task objects."""
    try:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            # Convert list of dicts back to list of objects
            return [Task(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty list if file doesn't exist or is empty
        return []

def add_task(tasks):
    print("\n--- Add New Task ---")
    title = input("Enter Task Title: ")
    desc = input("Enter Description: ")
    print("Categories: Work, Personal, Urgent, Other")
    category = input("Enter Category: ")
    
    new_task = Task(title, desc, category)
    tasks.append(new_task)
    print(f"Task '{title}' added successfully!")

def view_tasks(tasks):
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks found.")
        return

    # Print header
    print(f"{'ID':<4} {'Title':<20} {'Category':<10} {'Status':<10} {'Description'}")
    print("-" * 60)

    for index, task in enumerate(tasks):
        status = "Done" if task.completed else "Pending"
        print(f"{index + 1:<4} {task.title:<20} {task.category:<10} {status:<10} {task.description}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter the ID of the task to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid ID.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter the ID of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Task '{removed.title}' deleted.")
        else:
            print("Invalid ID.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== Personal To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Save & Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

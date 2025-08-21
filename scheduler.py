import json
import argparse
import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file or return empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(title, desc, due_date):
    """Add a new task with title, description, and due date."""
    tasks = load_tasks()
    task_id = 1 if not tasks else tasks[-1]["id"] + 1

    try:
        datetime.strptime(due_date, "%Y-%m-%d")  # validate date
    except ValueError:
        print(Fore.RED + " ❌ Invalid date format. Use YYYY-MM-DD.")
        return

    new_task = {
        "id": task_id,
        "title": title,
        "description": desc,
        "due_date": due_date,
        "status": "Pending"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(Fore.GREEN + f" ✅ Task '{title}' added successfully!")

def list_tasks():
    """Display all tasks with reminders."""
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + " 📭 No tasks found.")
        return

    today = datetime.today().date()
    print(Fore.CYAN + "\n 📋 Your Tasks:")
    for task in tasks:
        due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        status_symbol = "✅" if task["status"] == "Completed" else "⏳"

        # Decide color and reminder
        # If the task is completed
        if task["status"] == "Completed":
            color = Fore.GREEN
            reminder = ""
        # If the due date has passed
        elif due_date < today:
            color = Fore.RED
            reminder = "⚠️  Overdue!"
        # If the task is due today
        elif due_date == today:
            color = Fore.YELLOW
            reminder = " ⏰ Due Today!"
        # Otherwise
        else:
            color = Fore.WHITE
            reminder = ""
        print(color + f"ID: {task['id']} | {status_symbol} {task['title']} | Due: {task['due_date']} | Status: {task['status']} {reminder}")
    print(Style.RESET_ALL)

def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print(Fore.GREEN + f" 🎉  Task '{task['title']}' marked as completed!")
            return
    print(Fore.RED + " ❌ Task ID not found.")

def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print(Fore.RED + " ❌ Task ID not found.")
        return

    save_tasks(updated_tasks)
    print(Fore.MAGENTA + f"🗑️  Task {task_id} deleted successfully.")


def main():
    parser = argparse.ArgumentParser(description="Simple Task Scheduler")
    parser.add_argument("--add", action="store_true", help="Add a new task")
    parser.add_argument("--title", type=str, help="Task title")
    parser.add_argument("--desc", type=str, help="Task description")
    parser.add_argument("--due", type=str, help="Due date (YYYY-MM-DD)")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--complete", type=int, help="Mark a task as completed by ID")
    parser.add_argument("--delete", type=int, help="Delete a task by ID")

    args = parser.parse_args()

    if args.add:
        if not args.title or not args.desc or not args.due:
            print(Fore.RED + " ❌ Please provide --title, --desc, and --due for adding a task.")
        else:
            add_task(args.title, args.desc, args.due)
    elif args.list:
        list_tasks()
    elif args.complete:
        complete_task(args.complete)
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
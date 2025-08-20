import json
import argparse
import os
from datetime import datetime

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
        print(" ❌ Invalid date format. Use YYYY-MM-DD.")
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
    print(f" ✅ Task '{title}' added successfully!")


def main():
    parser = argparse.ArgumentParser(description="Simple Task Scheduler")
    parser.add_argument("--add", action="store_true", help="Add a new task")
    parser.add_argument("--title", type=str, help="Task title")
    parser.add_argument("--desc", type=str, help="Task description")
    parser.add_argument("--due", type=str, help="Due date (YYYY-MM-DD)")

    args = parser.parse_args()

    if args.add:
        if not args.title or not args.desc or not args.due:
            print(" ❌ Please provide --title, --desc, and --due for adding a task.")
        else:
            add_task(args.title, args.desc, args.due)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
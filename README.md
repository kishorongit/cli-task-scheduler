# Task Scheduler (JSON-based)

A simple Python command-line task scheduler that allows users to add, view, and complete tasks. Tasks are stored in a 
local JSON file for persistence. This project demonstrates **Python file handling, JSON manipulation, and CLI-based user
interaction**.

---

## 📋 Features

- ✅ Add new tasks with title, description, and due date
- ✅ View all tasks in a formatted list
- ✅ Mark tasks as completed
- ✅ Delete tasks by ID
- ✅ Store tasks in a JSON file for persistence
- ✅ Error handling for invalid inputs and file operations
- ✅ Print a warning when a task is due today or overdue
- ✅ Highlight pending vs completed tasks for enhanced user experience
- ✅ Support recurring tasks

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `argparse`, `json`, `datetime`, `os`, `coloroma`

---

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/kishorongit/cli-task-scheduler.git
cd cli-task-scheduler
```

## 🚀 Usage

### Add a new task
```bash
python scheduler.py --add --title "Finish Assignment" --desc "Submit by tomorrow" --due "2025-08-20"
python scheduler.py --add --title "Finish Report" --desc "Prepare monthly report" --due 2025-08-21""
python scheduler.py --add --title "Prepare Slides" --desc "Presentation for Friday" --due 2025-08-22"

```

### Add a recurring daily task
```bash
python scheduler.py --add --title "Morning Workout" --desc "30 min exercise" --due 2025-08-20 --recurrence daily
```

### Add a weekly task
```bash
python scheduler.py --add --title "Team Meeting" --desc "Weekly sync-up" --due 2025-08-21 --recurrence weekly
```
### View all tasks
```bash
python scheduler.py --list
```

### Mark a task as complete
```bash
python scheduler.py --complete 2
```

### Delete a task
```bash
python scheduler.py --delete 3
```

## 📂 Project Structure
```pgsql
cli-task-scheduler/
├── scheduler.py
├── tasks.json
├── .gitignore
├── requirements.txt
└── README.md
```

## 🐛 Error Handling

- Empty or corrupted JSON file
- Invalid task ID
- Incorrect date format
- File I/O issues

## 📄 License

This project is licensed under the MIT License. Please read more at: [Exploring the MIT Open Source License: A 
Comprehensive Guide](https://test-mit-tlo.pantheonsite.io/understand-ip/exploring-mit-open-source-license-comprehensive-guide)

## 👤 Author

Your Name – [subedi-kishor](https://www.linkedin.com/in/subedi-kishor/)

GitHub: [kishorongit](https://github.com/kishorongit)
# Task Manager

A simple Python task management system for tracking and organizing tasks with due dates.

## Features

- Create tasks with titles and optional due dates
- Mark tasks as complete
- Track pending and overdue tasks
- Easy-to-use task management interface

## Installation

Clone this repository and import the `TaskManager` class from `task_manager.py`:

```python
from task_manager import TaskManager
```

## Usage

### Creating a Task Manager

```python
task_manager = TaskManager()
```

### Adding Tasks

```python
# Add a task without a due date
task_manager.add_task("Complete project documentation")

# Add a task with a due date
from datetime import datetime
task_manager.add_task("Submit report", due_date=datetime(2025, 7, 15))
```

### Managing Tasks

```python
# Get all pending tasks
pending_tasks = task_manager.get_pending_tasks()

# Get overdue tasks
overdue_tasks = task_manager.get_overdue_tasks()

# Mark a task as complete
task_manager.complete_task("Complete project documentation")
```

## Task Properties

Each task has the following properties:
- Title (required)
- Due date (optional)
- Completion status
- Overdue status (automatically calculated based on due date)

## API Reference

### TaskManager Class

- `add_task(title: str, due_date: Optional[datetime] = None)`: Adds a new task
- `get_pending_tasks()`: Returns a list of incomplete tasks
- `get_overdue_tasks()`: Returns a list of tasks past their due date
- `complete_task(title: str)`: Marks the specified task as complete

### Task Class

- `mark_complete()`: Marks the task as complete
- `is_overdue()`: Checks if the task is past its due date

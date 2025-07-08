from typing import List, Optional
from datetime import datetime

class Task:
    def __init__(self, title: str, due_date: Optional[datetime] = None):
        self.title = title
        self.completed = False
        self.created_at = datetime.now()
        self.due_date = due_date

    def mark_complete(self):
        self.completed = True

    def is_overdue(self) -> bool:
        if self.due_date:
            return datetime.now() > self.due_date
        return False

    def __repr__(self):
        return f"<Task title={self.title} completed={self.completed}>"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, due_date: Optional[datetime] = None) -> Task:
        task = Task(title, due_date)
        self.tasks.append(task)
        return task

    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.tasks if not task.completed]

    def get_overdue_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.is_overdue() and not task.completed]

    def complete_task(self, title: str) -> bool:
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.mark_complete()
                return True
        return False

    def __repr__(self):
        return f"<TaskManager tasks={len(self.tasks)}>"

# task_manager.py

from datetime import datetime
from typing import List, Optional

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
        return f"<Task title='{self.title}' completed={self.completed}>"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, due_date: Optional[datetime] = None) -> Task:
        task = Task(title, due_date)
        self.tasks.append(task)
        return task

    def view_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return
        print("\nTarefas:")
        for task in self.tasks:
            status = "✅" if task.completed else "⏳"
            overdue = "⚠️ Atrasada" if task.is_overdue() else ""
            print(f"- {task.title} [{status}] {overdue}")

# Instância global para ser usada em main.py
task_manager = TaskManager()  
  
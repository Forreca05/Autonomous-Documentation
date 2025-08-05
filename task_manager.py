from typing import List, Optional
from datetime import datetime

class Task:
    def __init__(self, title: str, due_date: Optional[datetime] = None):
        """Initializes a new task object with the given title and optional due date.
        
        Args:
            title (str): The title of the task.
            due_date (Optional[datetime]): The due date for the task. Defaults to None.
        
        Returns:
            None: This method doesn't return anything.
        """
        self.title = title
        self.completed = False
        self.created_at = datetime.now()
        self.due_date = due_date

    def mark_complete(self):
        self.completed = True

    def is_overdue(self) -> bool:
        """Checks if the task is overdue based on its due date.
        
        Returns:
            bool: True if the task is overdue, False otherwise.
        """
        if self.due_date:
            return datetime.now() > self.due_date
        return False

    def __repr__(self):
        return f"<Task title={self.title} completed={self.completed}>"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, due_date: Optional[datetime] = None) -> Task:
        """Adds a new task to the task list.
        
        Args:
            title (str): The title of the task.
            due_date (Optional[datetime], optional): The due date of the task. Defaults to None.
        
        Returns:
            Task: The newly created task object.
        """
        task = Task(title, due_date)
        self.tasks.append(task)
        return task

    def get_pending_tasks(self) -> List[Task]:
        """Get a list of pending tasks.
        
        Returns:
            List[Task]: A list of Task objects that have not been completed.
        """
        return [task for task in self.tasks if not task.completed]

    def get_overdue_tasks(self) -> List[Task]:
        """Returns a list of overdue and incomplete tasks.
        
        Args:
            self: The instance of the class containing the tasks.
        
        Returns:
            List[Task]: A list of Task objects that are both overdue and not completed.
        """
        return [task for task in self.tasks if task.is_overdue() and not task.completed]

    def complete_task(self, title: str) -> bool:
        """Completes a task with the given title if it exists and is not already completed.
        
        Args:
            title (str): The title of the task to be completed.
        
        Returns:
            bool: True if the task was found and completed, False otherwise.
        """
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.mark_complete()
                return True
        return False

    def __repr__(self):
        return f"<TaskManager tasks={len(self.tasks)}>"

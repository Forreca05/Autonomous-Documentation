from typing import List, Optional
from datetime import datetime

class Task:
    """
    Represents a single to-do task.

    @class Task
    @var title: str The title or description of the task.
    @var completed: bool Flag indicating whether the task is completed.
    @var created_at: datetime Timestamp when the task was created.
    @var due_date: Optional[datetime] Optional deadline for the task.
    """

    def __init__(self, title: str, due_date: Optional[datetime] = None):
        """
        Initialize a new Task instance.

        @param title: str The title or description of the task.
        @param due_date: Optional[datetime] The deadline for the task, if any.
        """
        self.title = title
        self.completed = False
        self.created_at = datetime.now()
        self.due_date = due_date

    def mark_complete(self):
        """
        Mark this task as completed.

        @return: None
        """
        self.completed = True

    def is_overdue(self) -> bool:
        """
        Check whether the task is past its due date and still not completed.

        @return: bool True if the current date/time is past due_date, False otherwise.
        """
        if self.due_date:
            return datetime.now() > self.due_date
        return False

    def __repr__(self):
        """
        Provide a string representation of the Task object.

        @return: str Formatted string showing title and completion status.
        """
        return f"<Task title={self.title} completed={self.completed}>"


class TaskManager:
    """
    Manages a collection of Task instances.

    @class TaskManager
    @var tasks: List[Task] The list of tasks being managed.
    """

    def __init__(self):
        """
        Initialize a new TaskManager with an empty task list.

        @return: None
        """
        self.tasks: List[Task] = []

    def add_task(self, title: str, due_date: Optional[datetime] = None) -> Task:
        """
        Create a new task and add it to the manager.

        @param title: str The title or description of the new task.
        @param due_date: Optional[datetime] The deadline for the new task.
        @return: Task The newly created Task instance.
        """
        task = Task(title, due_date)
        self.tasks.append(task)
        return task

    def get_pending_tasks(self) -> List[Task]:
        """
        Retrieve all tasks that are not yet completed.

        @return: List[Task] List of tasks with completed == False.
        """
        return [task for task in self.tasks if not task.completed]

    def get_overdue_tasks(self) -> List[Task]:
        """
        Retrieve all tasks that are overdue and not completed.

        @return: List[Task] List of tasks where is_overdue() is True and completed == False.
        """
        return [task for task in self.tasks if task.is_overdue() and not task.completed]

    def complete_task(self, title: str) -> bool:
        """
        Mark the first matching task with the given title as complete.

        @param title: str The title of the task to mark complete.
        @return: bool True if a matching pending task was found and marked complete, False otherwise.
        """
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.mark_complete()
                return True
        return False

    def __repr__(self):
        """
        Provide a string representation of the TaskManager object.

        @return: str Formatted string showing the number of tasks being managed.
        """
        return f"<TaskManager tasks={len(self.tasks)}>"

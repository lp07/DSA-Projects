# TaskManager class represents a Simple Task Management System using Arrays

class TaskManager:
    def __init__(self, capacity):
        # Initialize an array to store tasks with a specified capacity
        self.tasks = [None] * capacity
        self.capacity = capacity
        self.size = 0

    # Method to Add task to the Task Manager.
    def add_task(self, task):
        # Check if there is space in the array to add a new task
        if self.size < self.capacity:
            # Add the task to the array and update the size
            self.tasks[self.size] = task
            self.size += 1
            print(f"Task '{task}' added successfully.")

        else:
            print("Task Manager is full. Cannot add more tasks.")

    # Method to Remove a task from Task Manager.
    def remove_task(self, task):
        # Check if task exists in the array
        if task in self.tasks:
            # Find the index of a task, mark it None, and update the size
            index = self.tasks.index(task)
            self.tasks[index] = None
            self.size -= 1
            print(f"Task '{task} removed successfully.")

        else:
            print(f"Task '{task}' not found.")

    # Method to display all the tasks in the Task Manager.
    def display_tasks(self):
        print("Tasks:")
        # Iterate through the array and print non-empty tasks
        for task in self.tasks:
            if task is not None:
                print(f" - {task}")
            print()

if __name__ == "__main__":

    # Create Task Manager instance with a capacity of 10
    task_manager = TaskManager(10)
    task_manager.add_task("Learn DSA")
    task_manager.add_task("Build a project using arrays")
    task_manager.add_task("Practice Algorithms")
    task_manager.add_task("Build projects using DSA")

    task_manager.remove_task("Build a project using arrays")
    task_manager.display_tasks()


















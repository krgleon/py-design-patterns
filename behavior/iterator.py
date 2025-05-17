class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def add(self, task):
        self.subtasks.append(task)

    def __iter__(self):
        return TaskIterator(self)

class TaskIterator:
    def __init__(self, root_task):
        self.stack = [(root_task, 0)]  # stack of (task, depth)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        task, depth = self.stack.pop()
        for subtask in reversed(task.subtasks):
            self.stack.append((subtask, depth + 1))
        return ("  " * depth) + f"- {task.name}"

project = Task("Build Web App")
frontend = Task("Frontend")
backend = Task("Backend")
auth = Task("Auth")
db = Task("Database")

backend.add(auth)
backend.add(db)
project.add(frontend)
project.add(backend)

for line in project:
    print(line)

from dataclasses import dataclass
import os


@dataclass
class WorkspaceManager:
    task_name: str

    def task_setup(self):
        print(self.task_name)
        taskpath = os.path.join(os.getcwd(), self.task_name)
        os.makedirs(taskpath, exist_ok=True)

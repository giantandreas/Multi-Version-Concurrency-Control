from typing import List
from mvccTransaction import Task

class Schedule:

    def __init__(self, schedule:List[Task]) -> None:
        self.tasks = schedule

    def execute_schedule(self):
        for task in self.tasks:
            print(task.transaction.name + " " + task.type + " " + task.target.name)
            task.execute()




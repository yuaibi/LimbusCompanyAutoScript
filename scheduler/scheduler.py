from tasks.daily_task import DailyTask

class Scheduler:

    def __init__(self):

        self.tasks = []

        self.tasks.append(DailyTask(self))

    def run(self):

        while True:

            for task in self.tasks:
                task.run()
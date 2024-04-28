from threading import Thread

from .work_queue import WorkQueue


class Server(Thread):
    """
    Creates individual server threads that synchronize using given queue and consume its tasks.
    """
    def __init__(self, sid: int, wq: WorkQueue) -> None:
        self.id = sid
        self.wq = wq

        Thread.__init__(self)

    def run(self) -> None:
        while True:
            if self.wq.check_end():
                # Execution is over, kill thread
                break

            elif next_task := self.wq.get_task_for_sid(self.id):
                # Execute task
                print(f'\tServer: {self.id}, served: {next_task}.')

from threading import Lock, Event
from queue import Queue


class WorkQueue:
    """
    Supports adding/receiving queued tasks.
    Also enables external load balancer & server threads to synchronize safely.
    """
    def __init__(self, event: Event):
        self.q = Queue()
        self.next_sid = None
        self.lock = Lock()
        self.event = event

    def add_task(self, task: str):
        """Adds task to queue."""
        with self.lock:
            self.q.put(task)

    def get_task_for_sid(self, sid):
        """Retrieves task from queue."""
        with self.lock:
            if self.next_sid == sid and not self.q.empty():
                next_task = self.q.get()
                self.next_sid = None
            else:
                next_task = None

        return next_task

    def set_next_worker(self, sid):
        with self.lock:
            if self.next_sid is None:
                self.next_sid = sid
                return True
            return False

    def stop_threads(self):
        """Notifies any threads working with queue, to terminate."""
        with self.lock:
            self.event.set()

    def re_enable(self):
        """Notifies any threads working with queue, to terminate."""
        with self.lock:
            self.event.clear()
            self.next_sid = None

    def get_tasks_num(self):
        """Returns size(approximation-multithread-exec). Mostly for debugging purposes."""
        with self.lock:
            return self.q.qsize()

    def check_end(self):
        """Helper, returns thread execution end condition."""
        with self.lock:
            return self.event.is_set()
